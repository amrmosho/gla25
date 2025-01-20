class ins_json_editor {
  options = {};
  constructor(o) {
    this.options = o;
  }

  _update() {
    var v = this.options.o._getvalue();
    var v = JSON.parse(v);
    var textedJson = JSON.stringify(v, undefined, 2);
    this.options.o._setvalue(textedJson);
  }
  _out() {
    var t = this;
    t._update();
    this.options.o._on("focusout", function () {
      t._update();
    });
  }
}
