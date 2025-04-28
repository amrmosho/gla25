from ins_kit._engine._bp import App
from flask import request
from werkzeug.utils import secure_filename
import os


class AjxUpload(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    UPLOAD_FOLDER = '/ins_web/ins_uploads/'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

    def allowed_file(slelf, filename):
        a= slelf.ins._server._post()
      
        if  "exts" in  slelf.ins._server._post():
           slelf.ALLOWED_EXTENSIONS= slelf.ins._server._post("exts")
           
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in slelf.ALLOWED_EXTENSIONS

    def get_size(fobj):
        if fobj.content_length:
            return fobj.content_length

        try:
            pos = fobj.tell()
            fobj.seek(0, 2)  # seek to end
            size = fobj.tell()
            fobj.seek(pos)  # back to original position
            return size
        except (AttributeError, IOError):
            pass

        # in-memory file object that doesn't support seeking or tell
        return 0  # assume small enough

    def upload_file(self):

        out = {}
        if request.method == 'POST':
            file = request.files['uploads']

        if file.filename == '':
            return {"status": "-1", "msg": f'No selected file'}


        if not self.allowed_file(file.filename):
            return {"status": "-1", "msg": f"file not allowed : {file}"}

        if file and self.allowed_file(file.filename):

            # file.save(os.path.join(self.UPLOAD_FOLDER, filename))

           # current_app.config['MAX_CONTENT_LENGTH'] = 16
            filename = secure_filename(file.filename)

            cwd = os.getcwd()
            dir = request.form.get("dir", "")
            if dir != "" and dir[-1] != '/':
                dir = dir+"/"

            directory = f"{cwd}{self.UPLOAD_FOLDER}{dir}"
            try:
                # Create directory if needed, ignoring already existing ones
                os.makedirs(directory, exist_ok=True)
            except OSError as e:
                return {"status": "-1", "msg": f"Failed to create directory: {e}"}

            size = 3
            if "size" in request.form:
                size = int(request.form["size"])
            max_size = (size * 1024 * 1024)

            if file.content_length > max_size:
                return {"status": "-1", "msg": f"File exceeded maximum allowed size"}
            
            
            out["oname"] = filename
            filename=f"{self.ins._data.unid}__{filename}"
            file.save(f"{cwd}{self.UPLOAD_FOLDER}{dir}{filename}")
            out["status"] = "1"
            out["name"] = filename
            out["path"] = dir+filename
            out["fullpath"] = self.UPLOAD_FOLDER+dir+filename
            out["type"] = filename.rsplit('.', 1)[1].lower()

        return self.ins._json._encode(out)

    def out(self):
        return "AjxUpload"
