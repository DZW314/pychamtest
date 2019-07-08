var SinConf = function () {
    return {
	edition: 3,
	mainHost: {"desktop":"https://www.manhuadui.com/","phone":"https://m.manhuadui.com/"},
        apiHost: 'https://450.manhuadang.net',
        resHost: [{"name":"自动选择","domain":["https://res.333dm.com"]},{"name":"电信线路","domain":["https://res02.333dm.com"]}],
        scheduler: "on",
        theme: {"basic":"dmzj","dmzj":{"background":{"mode":"rand","images":["mhd7.jpg","mhd8.jpg"]}}},
        common: [],
        desktop: {"chapter":{"mode":"pagination","reload":true,"maxPreload":10,"imageWidth":"auto"}},
        phone: {"chapter":{"mode":"pagination","reload":true,"maxPreload":10,"imageWidth":"auto"}},
        hotKeys: {"back":"backspace","read":"r","next":"right","prev":"left","nextChapter":"x","prevChapter":"z"},
        toastPosition: 'toast-top-center',
        toastClose: true,
        init: function () {
        }
    };
}();

toastr.options.positionClass = SinConf.toastPosition;
toastr.options.closeButton = SinConf.toastClose;

