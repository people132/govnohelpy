import sqlite3
from flask import Flask, render_template


app = Flask(__name__, template_folder='pages')

@app.route('/')
def get_main_page():
	return render_template('main_page.html')

app.run()