from flask import Flask, render_template, request, g
import requests
import json
from sqlalchemy import *
from sqlalchemy.pool import NullPool

application = Flask(__name__)

DATABASEURI = "postgresql://kl2844:PKKNNH@w4111db.eastus.cloudapp.azure.com/kl2844"
engine = create_engine(DATABASEURI)

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
	cursor = g.conn.execute("SELECT name, description FROM Event_Locates LIMIT 6")
	context['events'] = [event for event in cursor]
	cursor.close()
	cursor = g.conn.execute("SELECT name, location FROM Venues LIMIT 6")
	context['venues'] = [venue for venue in cursor]
	cursor.close()
	cursor = g.conn.execute("SELECT name, type, image FROM Performers LIMIT 60")
	context['performers'] = [performer for performer in cursor if performer['image'] != 'None'][:6]
	cursor.close()
	return render_template('index.html', **context) 

@application.route('/<list_name>')
def events_list(list_name=None):
	return render_template('lists.html', name = list_name) 

@application.route('/event/<id>')
def event(id=None):
	print id
	return render_template('details.html', id = id) 


@application.route('/surround')
def surround():
	lat = request.args.get('lat')
	lon = request.args.get('long')

	r = requests.get('http://52.1.34.124:9200/tweetmaps/tweets/_search', json = payload)
	return r.text

if __name__ == '__main__':
	application.run(debug=True)