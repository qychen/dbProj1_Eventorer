import argparse
import json
import pprint
import sys
import urllib
import urllib2
import random
import oauth2


API_HOST = 'api.yelp.com'
SEARCH_LIMIT = 3
SEARCH_PATH = '/v2/search/'

# OAuth credential placeholders that must be filled in by users.
CONSUMER_KEY = 'v8hQtU71-F5TEM3LI3CsDg'
CONSUMER_SECRET = '4bbgw3Qoe9bSTrxS-SdqfO3g3K4'
TOKEN = 'BVuxqKPCapDIxd4GA1M1hFe7nUG_uFin'
TOKEN_SECRET = 'I_xu-Y0RMFgOoZCZp1DY2ULUiM8'


def request(host, path, url_params=None):
    """Prepares OAuth authentication and sends the request to the API.

    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        url_params (dict): An optional set of query parameters in the request.

    Returns:
        dict: The JSON response from the request.

    Raises:
        urllib2.HTTPError: An error occurs from the HTTP request.
    """
    url_params = url_params or {}
    url = 'https://{0}{1}?'.format(host, urllib.quote(path.encode('utf8')))

    consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
    oauth_request = oauth2.Request(
        method="GET", url=url, parameters=url_params)

    oauth_request.update(
        {
            'oauth_nonce': oauth2.generate_nonce(),
            'oauth_timestamp': oauth2.generate_timestamp(),
            'oauth_token': TOKEN,
            'oauth_consumer_key': CONSUMER_KEY
        }
    )
    token = oauth2.Token(TOKEN, TOKEN_SECRET)
    oauth_request.sign_request(
        oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
    signed_url = oauth_request.to_url()

    print u'Querying {0} ...'.format(url)

    conn = urllib2.urlopen(signed_url, None)
    try:
        response = json.loads(conn.read())
    finally:
        conn.close()

    return response


def search(lat, lon):
    """Query the Search API by a search term and location.

    Args:
        term (str): The search term passed to the API.
        location (str): The search location passed to the API.

    Returns:
        dict: The JSON response from the request.
    """
    url_params = {
        'term': 'restaurant',
        'll': lat + ',' + lon, 
        'limit': SEARCH_LIMIT
    }
    return request(API_HOST, SEARCH_PATH, url_params=url_params)


# get the vid and coordinates of venues

f_venue = open('../data/Venues.txt','r')
rets = []

for line in f_venue.readlines():

	tmp = line.split('\t')
	tup = tmp[-2].split(',')
	lat = tup[0][1:]
	lon = tup[1][:-1]
	rets.append((tmp[0], lat, lon))

f_venue.close()



f_nearby = open('../data/Nearby.txt', 'w')
f_restaurant = open('../data/Restaurants.txt', 'w')

rids = dict()
rid = 1

count = 0
for (vid, lat, lon) in rets:

		try:
			rets = search(lat, lon)['businesses']

			for ret in rets:

				if not ret['id'] in rids:
					rids[ret['id']] = str(rid)
					if 'image_url' in ret:
						image = ret['image_url']
					else:
						image = ''
					f_restaurant.write(('\t'.join([str(rid), ret['name'], ','.join(ret['location']['display_address']), image, str(ret['rating'])]) + '\n').encode('utf-8'))
					rid += 1

				f_nearby.write((vid + '\t' + rids[ret['id']] + '\t' + str(random.random() * 4.5 + 0.5) + '\n').encode('utf-8'))
			print count
			count += 1
		except:
			pass


f_nearby.close()
f_restaurant.close()








