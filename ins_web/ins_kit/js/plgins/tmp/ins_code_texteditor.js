/**
 *
 * @param {type} options {title:$title,url:$url ,style:$style ,class:$class,data:$data,onclose:function(){},onopen:function(){}}
 * @returns {undefined}
 */
export class ins_code_texteditor {
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


    _out() {


        var id = this.options["name"];
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