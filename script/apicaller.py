import requests
import json
import random

import faker
from faker import Factory
import random
import string


req = requests.get('https://api.seatgeek.com/2/events?geoip=true&range=2000mi&per_page=2000&listing_count.gt=0')

events = json.loads(req.text)['events']

f_event = open('../data/Event_Locates.txt','w')
f_ticket = open('../data/Has_Tickets.txt','w')
f_performer = open('../data/Performers.txt','w')
f_venue = open('../data/Venues.txt','w')
f_perform = open('../data/Performs.txt','w')
terms = []
venues = []
perfms = []
t_ids = []
u_ids = []
e_ids = []
for event in events:
  taxonomies = ''
  #for term in event['taxonomies']:
  #  taxonomies = taxonomies + term['name'] + ','
  taxonomies = event['taxonomies'][0]['name']
  terms.append(taxonomies)
  e_ids.append(event['id'])
  f_event.write(str(event['id'])+'\t'+str(event['venue']['id'])+'\t'+event['title']+'\t'+event['type']+'\t'+\
    taxonomies+'\n')

  tid = random.randrange(10000,70000)
  while tid in t_ids:
    tid = random.randrange(10000,70000)
  t_ids.append(tid)
  f_ticket.write(str(event['id'])+'\t'+str(tid)+'\t'+\
    str(event['stats']['listing_count'])+'\t'+\
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


fake = Factory.create()

f_user = open('../data/Users.txt','w')
f_part = open('../data/Participates.txt','w')
f_favor = open('../data/Favors.txt','w')


for _ in range(2000):
  uid = random.randrange(20000,40000)
  while uid in u_ids:
    uid = random.randrange(20000,40000)
  u_ids.append(uid)
  f_user.write(str(uid)+'\t'+fake.name()+'\t'+\
    ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(15))\
    +'\t'+str(fake.date_time_between(start_date="-60y", end_date="-10y"))+'\t'+fake.email()+'\n')

for i in range(len(u_ids)):
  num = random.randrange(0,7)
  idxs = []
  for j in range(num):
    index = random.randrange(0,len(e_ids))
    while index in idxs:
      index = random.randrange(0,len(e_ids))
    idxs.append(index)
    f_part.write(str(u_ids[i])+'\t'+str(e_ids[index])+'\t'+str(random.randrange(0,3))+'\n')


for i in range(len(u_ids)):
  num = random.randrange(0,20)
  idxs = []
  for j in range(num):
    index = random.randrange(0,len(t_ids))
    while index in idxs:
      index = random.randrange(0,len(t_ids))
    idxs.append(index)
    f_favor.write(str(u_ids[i])+'\t'+str(t_ids[index])+'\t'+\
      str(fake.date_time_between(start_date="-2y", end_date="now"))+'\n')



