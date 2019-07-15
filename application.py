from flask import Flask, render_template

application = app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inquiries')
def inquiries():
	return render_template('inquiries.html')