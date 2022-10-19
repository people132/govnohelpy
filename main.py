import sqlite3
from flask import Flask, render_template

class QueueRequests:
	def __init__(self):
		self.conn = sqlite3.connect('bases/queue.db')
		self.cur = self.conn.cursor()

	def close(self):
		self.conn.commit()
		self.conn.close()

	def add_query(self, login, query_id, date, language, skills, years_months):
		insert_query = f'INSERT INTO Queue VALUES ("{login}", "{query_id}", "{date}", "{language}", "{skills}", "{years_months}")'
		self.cur.execute(insert_query)

	def pop_query(self, query_id):
		found = bool(self.cur.execute(f'SELECT login FROM Queue WHERE query_id = "{query_id}"').fetchall())
		delete_query = f'DELETE FROM Queue WHERE query_id = "{query_id}"'
		self.cur.execute(delete_query)
		return found

	def get_first(self, x: int):
		select_query = f'SELECT * FROM Queue LIMIT {x}'
		return self.cur.execute(select_query).fetchall()


queue = QueueRequests()

app = Flask(__name__, template_folder='pages')

@app.route('/moderator/')
def get_moderator_page():
	return render_template('moderator.html')

app.run()