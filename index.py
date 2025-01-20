from flask import  Blueprint, render_template
from ins_kit.ins import ins


area = "home"


ahome = Blueprint(area, __name__, template_folder=f"{ins._map.WEB_FOLDER}/{ins._map.TEMPLATES_FOLDER}/",
                  static_folder=ins._map.WEB_FOLDER)
@ahome.errorhandler(500)
def page_not_found(error):
    t=  error.description
    return render_template("tmp_admin_style/error.html",   title=t["title"],   msg=t["msg"]), 500

@ahome.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@ahome.route('/<path:path>', methods=['GET', 'POST'])
def home(path):
    
    return ins._tmp._render(area,path)

    
