/**
 *
 * @param {type} options {title:$title,url:$url ,style:$style ,class:$class,data:$data,onclose:function(){},onopen:function(){}}
 * @returns {undefined}
 */
export class ins_plg_json_editor {
    options = {};

    editor = null;
    constructor(o) {
        this.options = o;
    }


    _search = function(val) {
        var slef = this;

        var searchQuery = new RegExp("^\\s*_6147bfbb74052") //new RegExp("^\\s*" + val)



        let cursor = slef.editor.getSearchCursor(searchQuery);
        if (cursor.findNext()) {
            slef.editor.setSelection(cursor.from(), cursor.to());
        }

    }

    _getfiles(callback) {


        var p = '/ins_web/ins_incs/codemirror/';

        var cssfiles = [
            p + "lib/codemirror.css",
            // p + "theme/mbo.css",
            p + "theme/neo.css",

            p + "addon/dialog/dialog.css",
            p + "addon/search/matchesonscrollbar.css",
            p + "addon/fold/foldgutter.css"

        ];

        cssfiles.forEach(function(f) {


            var head = document.getElementsByTagName('head')[0];
            var link = document.createElement('link');
            link.rel = 'stylesheet';
            link.type = 'text/css';
            link.href = f;
            link.media = 'all';
            head.appendChild(link);

        });


        var files = [

            p + "addon/fold/indent-fold.js",
            p + "addon/fold/brace-fold.js",
            p + "addon/fold/foldgutter.js",
            p + "addon/fold/foldcode.js",
            p + "addon/search/jump-to-line.js",
            p + "addon/search/matchesonscrollbar.js",
            p + "addon/scroll/annotatescrollbar.js",
            p + "addon/search/search.js",
            p + "addon/search/searchcursor.js",
            p + "addon/dialog/dialog.js",
            p + "addon/edit/matchbrackets.js",
            p + "addon/selection/active-line.js",
            p + "mode/javascript/javascript.js",
            p + "mode/scheme/scheme.js",
            p + "lib/codemirror.js",
        ];

        ins(files).filesLoad(function(a) {
            console.log("end");
            callback();

        })


    }


    _out() {

        var self = this;

        ins()._ui._addLoader();
        this._getfiles(function() {
            ins()._ui._removeLoader();

            self._run();
        })
    }
    _run() {

        var id = this.options["id"];

        var slef = this;
        var t = document.getElementById(id + "_textarea");

        slef.editor = CodeMirror.fromTextArea(t, {
            mode: { name: "javascript", json: true },
            lineNumbers: true,
            styleActiveLine: true,
            theme: "mbo",
            matchBrackets: true,
            lineWrapping: true,
            extraKeys: {
                "F8": function(cm) {


                    var j = JSON.stringify(JSON.parse(cm.getValue()), null, "\t");
                    cm.setValue(j);


                },


                "Ctrl-Q": function(cm) { cm.foldCode(cm.getCursor()); },
                "F11": function(cm) {
                    cm.setOption("fullScreen", !cm.getOption("fullScreen"));
                },
                "Esc": function(cm) {
                    if (cm.getOption("fullScreen")) cm.setOption("fullScreen", false);
                },
                "Alt-F": "findPersistent"
            },
            foldGutter: true,
            gutters: ["CodeMirror-linenumbers", "CodeMirror-foldgutter"],
        });



        slef.editor.on("change", function() {
            t.value = slef.editor.getValue();
        });




    }
}