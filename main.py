from flask import Flask

app = Flask(__name__)

@app.route('/')
def main_page():
	return open('pages/main_page.html').read()

app.run()