from barnum import gen_data
import json

f = open('Users_old.txt', 'r')
f_out = open('Users.txt', 'w')

for line in f.readlines():

	line = line.strip().split('\t')
	new_line = []
	new_line.append(line[0])
	new_line.append(line[1])
	new_line.append(line[2])
	info = {}
	info['birthday'] = str(gen_data.create_birthday(min_age=18, max_age=60))
	info['email'] = gen_data.create_email(tld="com")
	info['mobile'] = gen_data.create_phone()
	tmp = gen_data.create_city_state_zip()
	info['city'] = tmp[1] + ', ' + tmp[2]
	new_line.append(json.dumps(info))
	f_out.write('\t'.join(new_line) + '\n')

f.close()
f_out.close()



