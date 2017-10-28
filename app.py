from flask import Flask,render_template,url_for,redirect,flash

app = Flask(__name__)


@app.route('/')
def login():
	return render_template('login.html')


@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/dashboard')
def dashboard():
	return render_template('dashboard.html')

@app.route('/created_recipes')
def created_recipes():
	return render_template('created_recipes.html')

if __name__ == '__main__':
	app.run(debug=True)
