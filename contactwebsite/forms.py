from flask_wtf import FlaskForm
from wtforms import BooleanField, SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, ValidationError
from contactwebsite.models import User

class RegisterationForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	panel = SelectField('Panel', choices=[('p1','Panel 1'),('p2','Panel 2')])
	participate = BooleanField('Participate in the event', validators=[DataRequired()])
	about = TextAreaField('Write about yourself', validators=[DataRequired()])
	submit = SubmitField('Submit')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('Email Id is already taken')
