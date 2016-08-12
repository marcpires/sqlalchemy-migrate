from flask import Blueprint,render_template

usuarios = Blueprint('usuarios', __name__)
usuarios.holder = 'blablabla'

def set_bla():
	usuarios.holder = 'anti-bla'

usuarios.before_request(set_bla)

@usuarios.route("/usuarios/")
def index():
	return render_template("usuarios/index.html", holder=usuarios.holder)