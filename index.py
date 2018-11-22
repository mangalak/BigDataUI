from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
class RegressionForm():
    parameter1 = TextField('Parameter 1:', validators=[validators.required()])
    parameter2 = TextField('Parameter 2:', validators=[validators.required(), validators.Length(min=6, max=35)])
    parameter3 = TextField('Parameter 3:', validators=[validators.required(), validators.Length(min=3, max=35)])

class DecisionForm():
    parameter1 = TextField('Parameter 1:', validators=[validators.required()])
    parameter2 = TextField('Parameter 2:', validators=[validators.required(), validators.Length(min=6, max=35)])
    parameter3 = TextField('Parameter 3:', validators=[validators.required(), validators.Length(min=3, max=35)])
    parameter4 = TextField('Parameter 3:', validators=[validators.required(), validators.Length(min=3, max=35)])

@app.route('/')
def base():
	return render_template('base.html')

@app.route('/hello', methods=['GET', 'POST'])
def hello():

	if request.method == 'POST':
		result = request.form['algorithm']
		if result == "1":
			form = RegressionForm()
			return render_template('regression.html', form=form)
		elif result == "2":
			form = DecisionForm()
			return render_template('decision.html', form=form)

@app.route('/logresult', methods=['GET', 'POST'])
def logresult():
	if request.method == 'POST':
		result = request.form
		return render_template("logresult.html",result = result)


if __name__ == '__main__':
	app.run(debug = True)
