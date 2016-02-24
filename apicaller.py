import requests
import json

req = requests.get('https://api.seatgeek.com/2/events?geoip=true&range=2000mi&per_page=2000&listing_count.gt=0')

events = json.loads(req.text)['events']

f_event = open('data/Event_Locates.txt','w')
f_ticket = open('data/Has_Tickets.txt','w')
f_performer = open('data/Performers.txt','w')
f_venue = open('data/Venues.txt','w')
f_perform = open('data/Performs.txt','w')
terms = []
venues = []
perfms = []
for event in events:
  taxonomies = ''
  #for term in event['taxonomies']:
  #  taxonomies = taxonomies + term['name'] + ','
  taxonomies = event['taxonomies'][0]['name']
  terms.append(taxonomies)
  f_event.write(str(event['id'])+'\t'+str(event['venue']['id'])+'\t'+event['title']+'\t'+event['type']+'\t'+\
    taxonomies+'\n')

  f_ticket.write(str(event['id'])+'\t'+str(event['stats']['listing_count'])+'\t'+\
    str(event['stats']['average_price'])+'\t'+str(event['stats']['lowest_price'])+'\t' \
    +str(event['stats']['highest_price'])+'\t'+event['datetime_local']+'\t'+event['url']+'\n') 

  for performer in event['performers']:
    if performer['id'] not in perfms:
      f_performer.write(str(performer['id'])+'\t'+performer['name']+'\t'+performer['type']\
        +'\t'+str(performer['image'])+'\t'+performer['url']+'\n')
      perfms.append(performer['id'])
    f_perform.write(str(event['id'])+'\t'+str(performer['id'])+'\n')

  venue = event['venue']
  if venue['id'] not in venues:
    f_venue.write(str(venue['id'])+'\t'+venue['name']+'\t'+venue['address']+' '+venue['extended_address']\
      +'\t('+str(venue['location']['lat'])+','+str(venue['location']['lon'])+')\t'+venue['url']+'\n')
    venues.append(venue['id'])




f_event.close()