from flask import Flask, render_template, request
import requests
import json

application = Flask(__name__)

@application.route('/')
def main_page():
	return render_template('index.html') 

@application.route('/events')
def events_list():
	return render_template('details.html', payload = {"test":"data"}) 

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
	application.debug = True
	application.run()