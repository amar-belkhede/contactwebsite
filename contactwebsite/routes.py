from contactwebsite import app, db
from flask import render_template, flash, redirect, url_for
from contactwebsite.forms import RegisterationForm
from contactwebsite.models import User


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
	form = RegisterationForm()
	if form.validate_on_submit():
		user = User(name=form.name.data, email=form.email.data, panel=form.panel.data, 
		participate=form.participate.data, about=form.about.data)
		db.session.add(user)
		db.session.commit()
		flash('Your form is been submitted!!', 'success')
		return redirect(url_for('submitted'))
	return render_template('index.html', form=form)

@app.route("/submitted", methods=['GET', 'POST'])
def submitted():
	return render_template('submitted.html')