/**
 *
 * @param {type} options {title:$title,url:$url ,style:$style ,class:$class,data:$data,onclose:function(){},onopen:function(){}}
 * @returns {undefined}
 */
export class ins_plg_animation {
    options = {};
    constructor(o) {
        this.options = o;
    }
    _position = function(type, to, add, speed, callback) {
        if (ins(speed)._isEmpty()) {
            speed = 5;
        }
        if (ins(callback)._isEmpty()) {
            callback = function() {};
        }
        ins(this.o)
            ._get()
            .forEach(function(item) {
                var l = parseFloat(item.style[type]);
                let p = l;
                speed = speed / Math.abs(to);
                //  var add = true;
                let t = l + to;
                /* 
                                      if (parseFloat(t) > parseFloat(to)) {
                                      add = false;
                                      }*/
                var inr = setInterval(frame, speed);

                function frame() {
                    if (
                        (parseFloat(p) >= parseFloat(t) && add) ||
                        (parseFloat(p) <= parseFloat(t) && !add)
                    ) {
                        clearInterval(inr);
                        callback(item);
                    } else {
                        if (add) {
                            p += 5;
                        } else {
                            p -= 5;
                        }
                        item.style[type] = p + "px";
                    }
                }
            });
    };
    _fadeout = function(callback, speed) {
        if (speed == null) {
            speed = 5;
        }
        ins(this.o)
            ._get()
            .forEach(function(item) {
                item.style.opacity = 1;
                var i = setInterval(ch, speed);
                var to = 1;

                function ch() {
                    if (to <= 0) {
                        clearInterval(i);
                        callback(item);
                    } else {
                        to -= 0.01;
                        item.style.opacity = to;
                    }
                }
            });
        return ins(this.o);
    };
    _fadein = function(callback, speed) {
        if (speed == null) {
            speed = 5;
        }
        ins(this.o)
            ._get()
            .forEach(function(a) {
                a.style.opacity = 0;
                var i = setInterval(ch, speed);
                var to = 0;

                function ch() {
                    if (to >= 1) {
                        clearInterval(i);
                        callback(a);
                    } else {
                        to += 0.01;
                        a.style.opacity = to;
                    }
                }
            });
        return ins(this.o);
    };
    _height = function(h, addclass, removeclass, speed) {
        var o = ins(this.o);
        if (!ins(addclass)._isEmpty()) {
            o._addclass(addclass);
        }
        if (!ins(removeclass)._isEmpty()) {
            o._removeclass(removeclass);
        }
        if (isNaN(h)) {
            h = o._getData(h);
        }
        if (ins(speed)._isEmpty()) {
            speed = "0.3s ease-out";
        }
        o._css({ transition: speed, "overflow-y": "hidden" });
        o._css({ "max-height": h + "px" });
    };
    _toggle_height = function(actclass) {
        if (!ins(actclass)._isExists()) {
            actclass = "ins_opend";
        }
        var o = ins(this.o);
        if (o._hasclass(actclass)) {
            var m = "min_height";
            if (ins(o._getData(m))._isEmpty()) {
                m = 0;
            }
            o._animation._height(m, "", actclass);
        } else {
            o._animation._height("max_height", actclass);
        }
    };
    _toggle_css = function(from, to, speed, actclass) {
        if (!ins(actclass)._isExists()) {
            actclass = "ins_opend";
        }
        var o = ins(this.o);
        if (ins(speed)._isEmpty()) {
            speed = "0.3s ease-out";
        }
        o._css({ transition: speed, "overflow-y": "hidden" });
        if (o._hasclass(actclass)) {
            o._css(from);
            o._removeclass(actclass);
        } else {
            o._css(to);
            o._addclass(actclass);
        }
    };
    _down = function(options) {
        if (ins(options.from)._isEmpty()) {
            options.from = 100;
        }
        if (ins(options.to)._isEmpty()) {
            options.to = 0;
        }
        if (ins(options.speed)._isEmpty()) {
            options.speed = 5;
        }
        var inv = setInterval(frame, options.speed);

        function frame() {
            if (options.from == options.to) {
                clearInterval(inv);
                if (ins(options.ondone)._isExists()) {
                    options.ondone();
                }
            } else {
                options.from--;
                options.frame(options.from);
            }
        }
    };
    _up = function(options) {
        if (ins(options.from)._isEmpty()) {
            options.from = 0;
        }
        if (ins(options.to)._isEmpty()) {
            options.to = 100;
        }
        if (ins(options.speed)._isEmpty()) {
            options.speed = 5;
        }
        var inv = setInterval(frame, options.speed);

        function frame() {
            if (options.from == options.to) {
                clearInterval(inv);
                if (ins(options.ondone)._isExists()) {
                    options.ondone();
                }
            } else {
                options.from++;
                options.frame(options.from);
            }
        }
    };
}