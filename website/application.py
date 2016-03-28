from flask import Flask, render_template, request, g
import requests
import json
from sqlalchemy import *
from sqlalchemy.pool import NullPool

application = Flask(__name__)

DATABASEURI = "postgresql://kl2844:PKKNNH@w4111db.eastus.cloudapp.azure.com/kl2844"
engine = create_engine(DATABASEURI)

def get_sql(command, args=None):
	cursor = g.conn.execute(command, args)
	res = [event for event in cursor]
	cursor.close()
	return res

@application.before_request
def before_request():
	"""
	This function is run at the beginning of every web request 
	(every time you enter an address in the web browser).
	We use it to setup a database connection that can be used throughout the request

	The variable g is globally accessible
	"""
	try:
		g.conn = engine.connect()
	except:
		print "uh oh, problem connecting to database"
		import traceback; traceback.print_exc()
		g.conn = None

@application.teardown_request
def teardown_request(exception):
	"""
	At the end of the web request, this makes sure to close the database connection.
	If you don't the database could run out of memory!
	"""
	try:
		g.conn.close()
	except Exception as e:
		pass

@application.route('/')
def main_page():
	context = dict()
	context['events'] = get_sql("SELECT eid, name, description FROM Event_Locates LIMIT 6")
	context['venues'] = get_sql("SELECT vid, name, location FROM Venues LIMIT 6")
	context['performers'] = get_sql("SELECT pid, name, type, image FROM Performers LIMIT 60")
	context['performers'] = [performer for performer in context['performers'] if performer['image'] != 'None'][:6]
	return render_template('index.html', **context) 

@application.route('/events')
def events_list():
	page = request.args.get('p')
	payload = get_sql("SELECT eid, name, description FROM Event_Locates LIMIT 9 "+"OFFSET "+str(int(page)*9))
	return render_template('elists.html', page=page, payload=payload) 

@application.route('/venues')
def venues_list():
	page = request.args.get('p')
	payload = get_sql("SELECT vid, name, location FROM Venues LIMIT 9 "+"OFFSET "+str(int(page)*9))
	return render_template('vlists.html', page=page, payload=payload) 

@application.route('/performers')
def performers_list():
	page = request.args.get('p')
	payload = get_sql("SELECT pid, name, type, image FROM Performers LIMIT 9"+"OFFSET "+str(page*9))
	return render_template('plists.html', page=page, payload=payload) 

@application.route('/event/<id>')
def event(id=None):
	context = dict()
	context['event'] = get_sql("SELECT eid, name, description, category FROM Event_Locates WHERE eid=%s", id)[0]
	context['venues'] = get_sql("SELECT V.vid, V.name, V.location, V.coordinate FROM Event_Locates AS E, Venues AS V \
								WHERE E.eid=%s AND E.vid=V.vid", id)
	context['performers'] = get_sql("SELECT P.pid, P.name, P.type, P.image, P.url \
									 FROM Performers AS P, Performs AS T \
									 WHERE T.eid=%s AND P.pid=T.pid", id)
	context['tickets'] = get_sql("SELECT tid, listing_count, average_price, lowest_price, highest_price, happen_date, url \
								  FROM Has_Tickets \
								  WHERE eid=%s", id)
	return render_template('event.html', **context) 

@application.route('/venue/<id>')
def venue(id=None):
	context = dict()
	context['venue'] = get_sql("SELECT vid, name, location, coordinate FROM Venues \
								WHERE vid=%s", id)[0]
	context['resturants'] = get_sql("SELECT R.rid, R.name, R.address, R.image, R.rating, N.distance \
									 FROM Restaurants AS R, Nearby AS N \
									 WHERE N.vid=%s AND N.rid=R.rid \
									 ORDER BY distance ASC", id)
	context['reviews'] = get_sql("SELECT R.content, R.rating, U.uid, U.name \
								  FROM Reviews AS R, Users AS U \
								  WHERE R.uid=U.uid AND R.vid=%s", id)
	return render_template('venue.html', **context) 

@application.route('/performer/<id>')
def performer(id=None):
	context = dict()
	context['performer'] = get_sql("SELECT name, type, image, url FROM Performers \
								WHERE pid=%s", id)[0]
	context['events'] = get_sql("SELECT E.name, E.eid \
								 FROM Event_Locates AS E, Performers AS P, Performs AS T \
								 WHERE T.eid=E.eid AND T.pid=P.pid AND P.pid=%s", id)
	return render_template('performer.html', **context) 

@application.route('/login')
def login():
	username = request.args.get('usnm');
	password = request.args.get('pswd');
	users = get_sql("SELECT * FROM Users WHERE uid=%s AND password=%s", (username, password))
	if users:
		return "yes"
	else:
		return "no"

@application.route('/users/<id>')
def users(id=None):
	users = get_sql("SELECT * FROM Users WHERE uid="+id)
	return render_template('user.html', user = users[0]) 

@application.route('/search')
def search():
	keywords = request.args.get('keywords')
	context = dict()
	sql = "SELECT eid, name, description FROM Event_Locates WHERE name LIKE %s LIMIT 6"
	# sql = "SELECT eid, name, description FROM Event_Locates WHERE name LIKE '%" + keywords + "% LIMIT 6"
	# for c in cursor:
	# 	print c
	# print sql
	a = get_sql(sql, "%" + keywords + "%")
	print a
	return "ok"

if __name__ == '__main__':
	application.run(debug=True)