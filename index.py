from flask import Blueprint, render_template, send_from_directory, session
from ins_kit.ins import ins


area = "home"


ahome = Blueprint(area, __name__, template_folder=f"{ins._map.WEB_FOLDER}/{ins._map.TEMPLATES_FOLDER}/",
                  static_folder=ins._map.WEB_FOLDER)


@ahome.errorhandler(500)
def page_not_found(error):
    t = error.description
    return render_template("tmp_admin_style/error.html",   title=t["title"],   msg=t["msg"]), 500


@ahome.route('/insdonwload/<path:filename>')
def download_file(filename):

    id = ins._users._session_get("id")
    if id==None:
        return "file not found!"
    b: str = ins._data.xor_decrypt(filename, f"{id}133")
    fs = b.split("@@")

    if id==int(fs[0]):
        dir= ins._map.UPLOADS_FOLDER+fs[1]
        dir=dir.replace("/ins_web" ,"ins_web")
        return send_from_directory(dir,
                                fs[2], as_attachment=True)
    else:
        return "file not found!"


@ahome.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@ahome.route('/<path:path>', methods=['GET', 'POST'])
def home(path):

    return ins._tmp._render(area, path)
