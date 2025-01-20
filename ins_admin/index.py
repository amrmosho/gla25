from flask import Flask,g, Blueprint ,abort, render_template
from ins_kit.ins import ins

import werkzeug.exceptions as ex


area = "ins_admin"
tmp = f"../{area}/{ins._map.WEB_FOLDER}/{ins._map.TEMPLATES_FOLDER}"
static = f"../{area}/{ins._map.WEB_FOLDER}"

ins_admin_bp = Blueprint(area, __name__,
                         template_folder=tmp, static_folder=static)

@ins_admin_bp.errorhandler(500)
def page_not_found(error):
    t=  error.description
    return render_template("tmp_admin_style/error.html",   title=t["title"],   msg=t["msg"]), 500


@ins_admin_bp.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@ins_admin_bp.route('/<path:path>', methods=['GET', 'POST'])
def admin(path):
    return ins._tmp._login(area,path)
    #return ins._tmp._render(area,path)
    


    

