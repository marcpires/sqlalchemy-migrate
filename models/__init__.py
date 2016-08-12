from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80),unique=True)
	email = db.Column(db.String(225), unique=True)

	def __init__(self, name, email):
		self.name = name
		self.email = email