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

@application.route('/<list_name>')
def events_list(list_name=None):
	return render_template('lists.html', name = list_name) 

@application.route('/event/<id>')
def event(id=None):
	context = dict()
	content = get_sql("SELECT name, description, category FROM Event_Locates WHERE eid=")
	return render_template('event.html', id = id) 


@application.route('/surround')
def surround():
	lat = request.args.get('lat')
	lon = request.args.get('long')

	r = requests.get('http://52.1.34.124:9200/tweetmaps/tweets/_search', json = payload)
	return r.text

if __name__ == '__main__':
	application.run(debug=True)