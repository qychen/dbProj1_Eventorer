import faker
from faker import Factory
import random
import string

fake = Factory.create()

f_user = open('../data/Users.txt','w')
f_user = open('../data/Users.txt','w')
f_user = open('../data/Users.txt','w')

ids = []

for _ in range(200):
	uid = random.randrange(2000,4000)
	while uid in ids:
		uid = random.randrange(2000,4000)
	ids.append(uid)
	f_user.write(str(uid)+'\t'+fake.name()+'\t'+\
		''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(15))\
		+'\t'+str(fake.date_time_between(start_date="-60y", end_date="-10y"))+'\t'+fake.email()+'\n')