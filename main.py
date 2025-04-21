from flask import Flask, request
from ins_kit.ins import ins
from index import ahome
from ins_admin.index import ins_admin_bp
from ins_gla.index import ins_gla_bp


from ajax import ajax_bp


app = Flask(__name__)

app.secret_key = 'ins12345'
app.config['SESSION_TYPE'] = 'filesystem'


@app.before_request
def before_request():
    ins._eng._int(request.path)


app.register_blueprint(ahome, url_prefix=f"/")

app.register_blueprint(ins_admin_bp, url_prefix=f"/ins_admin")

app.register_blueprint(ins_gla_bp, url_prefix=f"/ins_gla")

app.register_blueprint(ajax_bp, url_prefix=f"/ins_ajax")


if __name__ == '__main__':
    app.run(debug=True)
 