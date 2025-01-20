export class ins_plg_users {
    options = {};
    // data = [];
    isopen = false;
    constructor(o) {
        this.options = o;
        this.options.multiaple = false;
    }
    logout(to = "/") {
        ins("ajx_users/logout")._ajax._ins_ajax({}, (o) => {
            window.location = to;
        })
    }

    set_settings(ops, ondone) {

        ins("ajx_users/set_settings")._ajax._ins_ajax(ops, (o) => {
            var c = JSON.parse(o);
            ondone(c)
        })
    }

    get_settings(ops, ondone) {

        ins("ajx_users/get_settings")._ajax._ins_ajax({ "name": ops["name"] }, (o) => {
            var c = JSON.parse(o)
            ondone(c)
        })

    }

    _out() {}
}