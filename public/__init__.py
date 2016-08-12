from flask import Blueprint, render_template
from models import User, db

public = Blueprint('public', __name__)

@public.route("/")
def index():
	total = User.query.count()
	return render_template("public/index.html", total=total)