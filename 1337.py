#!/usr/bin/python3
import tweepy, safygiphy, urllib, os

keysfile = open('keys.txt', 'r')
keys = keysfile.readlines()
CONSUMER_KEY = keys[0].rstrip()
CONSUMER_SECRET = keys[1].rstrip()
ACCESS_TOKEN = keys[2].rstrip()
ACCESS_TOKEN_SECRET = keys[3].rstrip()

print("Authenticating...")
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

giphy = safygiphy.Giphy()

attempts = 3
success = False

while success == False:
	print("Getting trending gifs...")
	gif = giphy.trending()
	print("Downloading gif...")
	urllib.request.urlretrieve(gif['data'][0]['images']['downsized']['url'], 'temp_gif.gif')

	try:
		print("Uploading tweet...")
		api.update_with_media('temp_gif.gif', """It's leet o'clock!""")
	except tweepy.TweepError as error:
		print("Something went wrong!")
		print(error)
		pass
	else:
		print("Success!")
		success = True
	
	os.remove('temp_gif.gif')
	attempts -= 1
	print("Remaining attempts: " + str(attempts))
	if attempts <= 0:
		print("Giving up.")
		success = True