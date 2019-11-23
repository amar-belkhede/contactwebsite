from contactwebsite import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20), nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	panel = db.Column(db.String(), nullable=False)
	participate = db.Column(db.Boolean, default=False, nullable=False)
	about = db.Column(db.Text, nullable=False)

	def __repr__(self):
		return f"User('{self.name}','{self.email}')"
