import random

# get the vid and coordinates of venues

pools = ['I was a small child when The Lion King first came out in theaters. None of that changed while I watched it on Broadway. The stampede was just as heart-clenching, Timon and Pumbaa were still as funny and silly.',
		'But what really captivated me was the opening sequence of the birth of Simba (I have chills just thinking about it) and the song Musafa sings to Simba. It is the thread that brings the individual sections of the musical together and I still can\'t get it out of my head.',
		'Rafiki was, as well, outstanding. And Scar was just as deliciously bad as he was as a cartoon. I would wholeheartedly recommend The Lion King to everyone!',
		'From start to finish the Lion King on Broadway was an exciting, awesome display of theatre!.',
		'This is the most amazing play I have ever seen. In the first two minutes, you are blown away by the stage characters. The production is truly a Disney show (first class all the way). I would highly recommend this to anyone.',
		'More than 70 million people around the world have come to discover the thrill, the majesty, the truly one-of-a-kind musical that is THE LION KING.',
		'I have now seen this musical 14 times, and it just gets better and better!',
		'This was our first Broadway play, and it was everything it was billed as and more. We had great seats, and it was an awesome atmosphere. It\'s been months since I laughed like that, and we had a great time, as did basically all of the audience.',
		'So I have been a wrestling fan for a long time. This was the first time I got a chance to go to a live event. It was nice to experience it live once, but I probably will just stick to watching it on tv.',
		'There was an energetic Chicago atmosphere as usual, but none of the matches took your breath away.',
		'Aladdin is one of the BEST shows I have ever seen on Broadway, and I\'ve seen quite a few. The costumes are stunning, the dancing is entertaining, and the jokes just keep coming!',
		'So much happened before Dorothy dropped in.',
		'So much happened before Dorothy dropped in.',
		'Performances are recommended for a general audience. As an advisory to adults who might bring children, Disney recommends its productions for ages 6 and up.',
		'2 hours and 30 minutes, with a 15-minute intermission',
		'More than 70 million people around the world have come to discover the thrill, the majesty, the truly one-of-a-kind musical that is THE LION KING.',
		'And there\'s no better place to experience this landmark entertainment event than in the city where it all began.',
		' For those like me who were remember seeing the original at the cinema as a child it was an incredible nostalgic journey into the story, portrayed very faithfully to the movie but adding it\'s own little touches',
		'And there\'s no better place to experience this landmark entertainment event than in the city where it all began. Join us at the Minskoff Theatre, in the heart of Times Square, and discover the pride of New York.',
		'don\'t want to give any spoilers so I\'ll just let it go!',
		'I cried and laughed and cheered for Simba.'
		]

f_venue = open('../data/Venues.txt','r')
rets = []

for line in f_venue.readlines():

	tmp = line.split('\t')
	rets.append((tmp[0], tmp[1]))

f_venue.close()

f_user = open('../data/Users.txt', 'r')
users = []

for line in f_user.readlines():

	users.append(line.split('\t')[0])

f_user.close()

rid = 1
f_reviews = open('../data/Reviews.txt', 'w')
for (vid, ret) in rets:

	if random.random() > 0.5:
		for _ in range(int(random.random() * 4)):

			rating = str(int(random.random() * 10))
			content = pools[int(random.random() * len(pools))]

			f_reviews.write(('\t'.join([str(rid), vid, str(users[int(random.random() * len(users))]), content, rating]) + '\n').encode('utf-8'))
			rid += 1
	# except:
	# 	pass
f_reviews.close()






