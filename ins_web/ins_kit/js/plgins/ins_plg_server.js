export class ins_plg_server {
    options = {};
    // data = [];
    isopen = false;
    constructor(o) {
        this.options = o;
        this.options.multiaple = false;
    }





    removeSession(ops, ondone) {
        ins("ajx_server/_remove_session")._ajax._ins_ajax({ "name": ops["name"] }, (o) => {
            window.location = to;
        })
    }



    getSession(ops, ondone) {
        ins("ajx_server/_get_session")._ajax._ins_ajax({ "name": ops["name"] }, (o) => {
            ondone(o)
        })
    }
    setSession(ops, ondone) {
        ins("ajx_server/_set_session")._ajax._ins_ajax(ops, (o) => {
            var c = JSON.parse(o)
            ondone(c)
        })
    }






    _out() {


    }
}