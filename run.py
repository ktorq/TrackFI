import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing

app = Flask(__name__)
SQLDB = 'dbs/trackfi.sqlite'


def connect_db():
	"""Connects to the specific database."""
	return sqlite3.connect(SQLDB)

@app.before_request
def before_request():
	try:
		g.db = connect_db()
	except:
		print("Doh! Error connecting to db")

@app.teardown_request
def teardown_request(exception):
	try:
		db = getattr(g, 'db', None)
		if db is not None:
			db.close()
	except:
		print("Doh! Error closing db")

@app.route('/')
@app.route('/home')
def home():
	user = {'nickname': 'Bob'}
	return render_template("home.html",
						   title='Home',
						   user=user)

@app.route('/accounts')
def accounts():
	cur = g.db.execute('select * from Accounts')
	entries = [dict(id=row[0], name=row[1]) for row in cur.fetchall()]
	return render_template("accounts.html",entries=entries)

@app.route('/transactions')
def transactions():
	cur = g.db.execute('select * from transactions')
	transactions = [dict(CreateDate=row[0], 
					Description=row[1],
					OriginalDescription=row[2], 
					Amount=row[3],
					TransactionType=row[4], 
					Category=row[5],
					AccountName=row[6], 
					Labels=row[7],
					Notes=row[8]) 
				for row in cur.fetchall()]
	return render_template("transactions.html",transactions=transactions)

if __name__ == "__main__":
	app.run(debug=True)