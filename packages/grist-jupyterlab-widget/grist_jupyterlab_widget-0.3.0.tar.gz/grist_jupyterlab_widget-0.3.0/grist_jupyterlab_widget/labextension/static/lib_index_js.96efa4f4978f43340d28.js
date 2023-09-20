"use strict";
(self["webpackChunkgrist_widget"] = self["webpackChunkgrist_widget"] || []).push([["lib_index_js"],{

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var comlink__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! comlink */ "webpack/sharing/consume/default/comlink/comlink");
/* harmony import */ var comlink__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(comlink__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _initKernelPy__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./initKernelPy */ "./lib/initKernelPy.js");
/* harmony import */ var _jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/docmanager */ "webpack/sharing/consume/default/@jupyterlab/docmanager");
/* harmony import */ var _jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_1__);



const pendingWorkers = [];
class MyWorker extends Worker {
    constructor(scriptURL, options) {
        super(scriptURL, options);
        const { grist } = window;
        if (grist) {
            exposeWorker(this, grist);
        }
        else {
            pendingWorkers.push(this);
        }
    }
}
window.Worker = MyWorker;
const emptyNotebook = {
    content: {
        'metadata': {
            'language_info': {
                'codemirror_mode': {
                    'name': 'python',
                    'version': 3
                },
                'file_extension': '.py',
                'mimetype': 'text/x-python',
                'name': 'python',
                'nbconvert_exporter': 'python',
                'pygments_lexer': 'ipython3',
                'version': '3.11'
            },
            'kernelspec': {
                'name': 'python',
                'display_name': 'Python (Pyodide)',
                'language': 'python'
            }
        },
        'nbformat_minor': 4,
        'nbformat': 4,
        'cells': [
            {
                'cell_type': 'code',
                'source': '',
                'metadata': {},
                'execution_count': null,
                'outputs': []
            }
        ]
    },
    format: 'json',
};
/**
 * Initialization data for the grist-widget extension.
 */
const plugin = {
    id: 'grist-widget:plugin',
    description: 'Custom Grist widget for a JupyterLite notebook',
    autoStart: true,
    requires: [_jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_1__.IDocumentManager],
    activate: (app) => {
        // Make sure there's a notebook file so it doesn't give a 404 error
        // if the grist plugin loads too slowly.
        app.serviceManager.contents.save('notebook.ipynb', emptyNotebook);
        hideBars(app).catch(e => console.error(e));
        const script = document.createElement('script');
        script.src = 'https://docs.getgrist.com/grist-plugin-api.js';
        script.id = 'grist-plugin-api';
        script.addEventListener('load', async () => {
            // await delay(1000);
            const grist = window.grist;
            app.serviceManager.contents.fileChanged.connect(async (_, change) => {
                var _a;
                if (change.type === 'save' && ((_a = change.newValue) === null || _a === void 0 ? void 0 : _a.path) === 'notebook.ipynb') {
                    grist.setOption('notebook', change.newValue);
                }
            });
            grist.ready();
            const notebook = await grist.getOption('notebook');
            if (notebook) {
                await app.serviceManager.contents.save('notebook.ipynb', notebook);
                // Immediately reload the notebook file, otherwise it will show a dialog
                // asking the user if they want to reload the file.
                await app.commands.execute('docmanager:reload');
            }
            console.log('JupyterLab extension grist-widget is activated!');
            const kernel = await getKernel(app);
            kernel.requestExecute({ code: _initKernelPy__WEBPACK_IMPORTED_MODULE_2__["default"] });
            for (const worker of pendingWorkers) {
                exposeWorker(worker, grist);
            }
            const records = await grist.fetchSelectedTable();
            await updateRecordsInKernel(app, records, { rerunCells: true });
            grist.onRecords(async (records) => {
                await updateRecordsInKernel(app, records, { rerunCells: false });
            });
        });
        document.head.appendChild(script);
    }
};
async function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
function exposeWorker(worker, grist) {
    comlink__WEBPACK_IMPORTED_MODULE_0__.expose({
        grist: {
            ...grist,
            getTable: (tableId) => comlink__WEBPACK_IMPORTED_MODULE_0__.proxy(grist.getTable(tableId))
        }
    }, worker);
}
async function getKernel(app) {
    var _a, _b;
    while (true) {
        const widget = app.shell.currentWidget;
        const kernel = (_b = (_a = widget === null || widget === void 0 ? void 0 : widget.context.sessionContext) === null || _a === void 0 ? void 0 : _a.session) === null || _b === void 0 ? void 0 : _b.kernel;
        if (kernel) {
            return kernel;
        }
        await delay(100);
    }
}
async function updateRecordsInKernel(app, records, { rerunCells }) {
    const kernel = await getKernel(app);
    const future = kernel.requestExecute({
        code: `__grist_records__ = ${JSON.stringify(records)}`
    });
    if (rerunCells) {
        let done = false;
        future.onIOPub = (msg) => {
            if (done) {
                return;
            }
            if (msg.header.msg_type === 'status' &&
                msg.content.execution_state === 'idle') {
                done = true;
                app.commands.execute('notebook:run-all-cells');
            }
        };
    }
}
async function hideBars(app) {
    while (!app.shell.currentWidget) {
        await delay(100);
    }
    const shell = app.shell;
    shell.collapseLeft();
    shell._titleHandler.parent.setHidden(true);
    shell._leftHandler.sideBar.setHidden(true);
    for (let i = 0; i < 1000; i++) {
        if (!shell.leftCollapsed) {
            shell.collapseLeft();
            shell._leftHandler.sideBar.setHidden(true);
            break;
        }
        else {
            await delay(10);
        }
    }
}
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);


/***/ }),

/***/ "./lib/initKernelPy.js":
/*!*****************************!*\
  !*** ./lib/initKernelPy.js ***!
  \*****************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
// language=Python
const code = `
def __make_grist_api():
    from pyodide.ffi import to_js
    import js
    import pyodide_js

    class ComlinkProxy:
        def __init__(self, proxy, name=None):
            self._proxy = proxy
            self._name = name

        def __getattr__(self, name):
            return ComlinkProxy(getattr(self._proxy, name), name)

        async def __call__(self, *args, **kwargs):
            args = [
                to_js(arg, dict_converter=js.Object.fromEntries)
                for arg in args
            ]
            kwargs = {
                key: to_js(value, dict_converter=js.Object.fromEntries)
                for key, value in kwargs.items()
            }
            result = await self._proxy(*args, **kwargs)
            if self._name == "getTable":
                result = ComlinkProxy(result)
            elif hasattr(result, "to_py"):
                result = result.to_py()
            return result

    js.importScripts("https://unpkg.com/comlink@4.4.1/dist/umd/comlink.js")
    pyodide_js.registerComlink(js.Comlink)
    return ComlinkProxy(js.Comlink.wrap(js).grist)


grist = __make_grist_api()
`;
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (code);


/***/ })

}]);
//# sourceMappingURL=lib_index_js.96efa4f4978f43340d28.js.map