# -*- coding: utf-8 -*-
from flask import Flask
from public import public as public_blueprint
from usuarios import usuarios as usuarios_blueprint
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask'

db.init_app(app)

app.register_blueprint(public_blueprint)

if __name__ == "__main__":
	app.run(debug=True)

