# coding=utf-8
import tinder_api as tinder
import features as api
import schedule
import time 
import json 
import random
from pymongo import MongoClient
db = MongoClient('mongodb://master:1234@ds129374.mlab.com:29374/kylestinder')



def matches():
    if tinder.authverif() == True: 
       matches = tinder.get_recommendations()
       return matches
    else: 
        print('Sorry, something went wrong')
        return None

def startAuto():
	schedule.every(24).hour.do(job)
	return None

def sendMsg(name, id): 
	 messages = ["So %s, Better Sunday adventure: Bottomless mimosas at Mikes Chicken and Doughnuts, hot pilates, churching it up or being stuck in an elevator with George Clooney?", "%s, lets just skip to the important stuff. What's your favorite Spice Girls song", "I just saw the best upsexy ever", "I want to paint you green and spank you like a disobedient avocado.", "Do you peel a banana from the top or bottom?", "You don't know how many times I had to swipe left to find you!", "Do you think love is real?", "Two truths and a lie; ready. set. go!", "You can only keep one: Jon Stewart, Stephen Colbert, or John Oliver?"] % (name)
	 random_message = random.choice(messages)
	 print(random_message)


def job():
	count = 0
	while count < 50: 
		women = matches()
		women = women['results']

		for w in women:
			tinder.like(w['_id'])
			print('liked')
			count += 1
			api.pause()
	
	nap_length = 3 * random.random()
	time.sleep(nap_length)

tinder.authverif()
m = api.get_match_info()

for k in m.iteritems():
	length = len(k)
	length -= 1
	
	# definitions to pass on 
	id = k[0]
	msgs = k[length]['messages']
	name = k[length]['name']

	print(k[length])
	if len(msgs) == 0:
		sendMsg(name, id)
		api.pause()



