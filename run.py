import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing

app = Flask(__name__)
SQLDB = 'dbs/trackfi.sqlite'

def round_two_dec(table,col):
    for x in range(len(table)):
        table[x][col] = round(table[x][col],2)

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
@app.route('/summary')
def summary():
	cur = g.db.execute('select * from Accounts')
	entries = [dict(id=row[0], name=row[1]) for row in cur.fetchall()]
	user = {'nickname': 'Bob'}
	return render_template("summary.html", title='Summary', user=user, entries=entries)

@app.route('/monthly')
def monthly():
	cur = g.db.execute('select * from Accounts')
	entries = [dict(id=row[0], name=row[1]) for row in cur.fetchall()]
	user = {'nickname': 'Bob'}
	return render_template("monthly.html", title='Monthly', user=user, entries=entries)

@app.route('/yearly')
def yearly():
	cur = g.db.execute('select * from Accounts')
	entries = [dict(id=row[0], name=row[1]) for row in cur.fetchall()]
	user = {'nickname': 'Bob'}
	return render_template("yearly.html", title='Yearly', user=user, entries=entries)

@app.route('/fi')
def fi():
	cur = g.db.execute('select * from Accounts')
	entries = [dict(id=row[0], name=row[1]) for row in cur.fetchall()]
	return render_template("fi.html",title='FI Projections',entries=entries)

@app.route('/recalc')
def recalc():
	cur = g.db.execute('select * from Accounts')
	entries = [dict(id=row[0], name=row[1]) for row in cur.fetchall()]
	return render_template("recalc.html",title='RE Calculator',entries=entries)

@app.route('/swr')
def swr():
	cur = g.db.execute('select * from Accounts')
	entries = [dict(id=row[0], name=row[1]) for row in cur.fetchall()]
	return render_template("swr.html",title='Safe Withdrawal Rate',entries=entries)

@app.route('/investments')
def investments():
	cur = g.db.execute('select * from Accounts')
	entries = [dict(id=row[0], name=row[1]) for row in cur.fetchall()]
	cur2 = g.db.execute('select * from allinvestments')
	overall = [dict(createdate=row[0], 
					account=row[1],
					contributed=row[2], 
					monthlyreturns=row[3],
					performance=row[4], 
					totals=row[5],
					monthchange=row[6], 
					ytdreturn=row[7],
					ytdroi=row[8],
					spcmonthlyreturn=row[9],
					performancevsspx=row[10]) 
					for row in cur2.fetchall()]
	return render_template("investments.html",title='Investments',entries=entries, overall=overall)

@app.route('/espp')
def espp():
	cur = g.db.execute('select * from Accounts')
	entries = [dict(id=row[0], name=row[1]) for row in cur.fetchall()]
	cur2 = g.db.execute('select * from allinvestments')
	overall = [dict(createdate=row[0],
					account=row[1],
					contributed=row[2],
					monthlyreturns=row[3],
					performance=row[4],
					totals=row[5],
					monthchange=row[6],
					ytdreturn=row[7],
					ytdroi=row[8],
					spcmonthlyreturn=row[9],
					performancevsspx=row[10])
					for row in cur2.fetchall()]
	return render_template("espp.html",title='ESPP',entries=entries, overall=overall)

@app.route('/taxable')
def taxable():
	cur = g.db.execute('select * from Accounts')
	entries = [dict(id=row[0], name=row[1]) for row in cur.fetchall()]
	cur2 = g.db.execute('select * from allinvestments')
	overall = [dict(createdate=row[0],
					account=row[1],
					contributed=row[2],
					monthlyreturns=row[3],
					performance=row[4],
					totals=row[5],
					monthchange=row[6],
					ytdreturn=row[7],
					ytdroi=row[8],
					spcmonthlyreturn=row[9],
					performancevsspx=row[10])
					for row in cur2.fetchall()]
	return render_template("taxable.html",title='Taxable',entries=entries, overall=overall)

@app.route('/401k')
def my401k():
	cur = g.db.execute('select * from Accounts')
	entries = [dict(id=row[0], name=row[1]) for row in cur.fetchall()]
	cur2 = g.db.execute('select * from allinvestments')
	overall = [dict(createdate=row[0],
					account=row[1],
					contributed=row[2],
					monthlyreturns=row[3],
					performance=row[4],
					totals=row[5],
					monthchange=row[6],
					ytdreturn=row[7],
					ytdroi=row[8],
					spcmonthlyreturn=row[9],
					performancevsspx=row[10])
					for row in cur2.fetchall()]
	return render_template("401k.html",title='401k',entries=entries, overall=overall)

@app.route('/ira')
def ira():
	cur = g.db.execute('select * from Accounts')
	entries = [dict(id=row[0], name=row[1]) for row in cur.fetchall()]
	cur2 = g.db.execute('select * from allinvestments')
	overall = [dict(createdate=row[0],
					account=row[1],
					contributed=row[2],
					monthlyreturns=row[3],
					performance=row[4],
					totals=row[5],
					monthchange=row[6],
					ytdreturn=row[7],
					ytdroi=row[8],
					spcmonthlyreturn=row[9],
					performancevsspx=row[10])
					for row in cur2.fetchall()]
	return render_template("ira.html",title='IRA',entries=entries, overall=overall)

@app.route('/cash')
def cash():
	cur = g.db.execute('select * from Accounts')
	entries = [dict(id=row[0], name=row[1]) for row in cur.fetchall()]
	cur2 = g.db.execute('select * from allinvestments')
	overall = [dict(createdate=row[0],
					account=row[1],
					contributed=row[2],
					monthlyreturns=row[3],
					performance=row[4],
					totals=row[5],
					monthchange=row[6],
					ytdreturn=row[7],
					ytdroi=row[8],
					spcmonthlyreturn=row[9],
					performancevsspx=row[10])
					for row in cur2.fetchall()]
	return render_template("cash.html",title='Cash',entries=entries, overall=overall)

@app.route('/debt')
def debt():
	cur = g.db.execute('select * from Accounts')
	entries = [dict(id=row[0], name=row[1]) for row in cur.fetchall()]
	cur2 = g.db.execute('select * from allinvestments')
	overall = [dict(createdate=row[0],
					account=row[1],
					contributed=row[2],
					monthlyreturns=row[3],
					performance=row[4],
					totals=row[5],
					monthchange=row[6],
					ytdreturn=row[7],
					ytdroi=row[8],
					spcmonthlyreturn=row[9],
					performancevsspx=row[10])
					for row in cur2.fetchall()]
	return render_template("debt.html",title='Debt',entries=entries, overall=overall)

@app.route('/income')
def income():
	cur = g.db.execute('select * from paychecks')
	paychecks = [dict(date=row[0], netpay=row[1], earnings=row[2], deductions=row[3], taxes=row[4]) for row in cur.fetchall()]
	round_two_dec(paychecks,'deductions')
	round_two_dec(paychecks,'taxes')
	return render_template("income.html",title='Income',paychecks=paychecks)

@app.route('/paychecks')
def paychecks():
	cur = g.db.execute('select * from paychecks')
	paychecks = [dict(date=row[0], netpay=row[1], earnings=row[2], deductions=row[3], taxes=row[4]) for row in cur.fetchall()]
	round_two_dec(paychecks,'deductions')
	round_two_dec(paychecks,'taxes')
	return render_template("paychecks.html",title='Paychecks',paychecks=paychecks)

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
	return render_template("transactions.html",title='Transactions',transactions=transactions)

@app.route('/categories')
def categories():
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
	return render_template("categories.html",title='Categories',transactions=transactions)

@app.route('/budget')
def budget():
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
	return render_template("budget.html",title='Budget',transactions=transactions)

if __name__ == "__main__":
	app.run(debug=True)