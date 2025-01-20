/**
 *
 * @param {type} options {title:$title,url:$url ,style:$style ,class:$class,data:$data,onclose:function(){},onopen:function(){}}
 * @returns {undefined}
 */
export class ins_plg_ {
    options = {};
    constructor(o) {
        this.options = o;
    }
    _out() {

        this.options.o._on("click", () => {


            alert("aaaa");
        })

    }
}