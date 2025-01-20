from flask import Flask,g, Blueprint ,abort, render_template
from ins_kit.ins import ins


area = "ins_gla"
tmp = f"../{area}/{ins._map.WEB_FOLDER}/{ins._map.TEMPLATES_FOLDER}"
static = f"../{area}/{ins._map.WEB_FOLDER}"

ins_gla_bp = Blueprint(area, __name__,
                         template_folder=tmp, static_folder=static)





@ins_gla_bp.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@ins_gla_bp.route('/<path:path>', methods=['GET', 'POST'])
def admin(path):
    return ins._tmp._login(area,path)


    

