import tweepy, giphypop, urllib, os

keysfile = open('keys.txt', 'r')
keys = keysfile.readlines()
CONSUMER_KEY = keys[0].rstrip()
CONSUMER_SECRET = keys[1].rstrip()
ACCESS_TOKEN = keys[2].rstrip()
ACCESS_TOKEN_SECRET = keys[3].rstrip()

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

gif = giphypop.random_gif()
urllib.request.urlretrieve(gif.media_url, 'temp_gif.gif')

api.update_with_media('temp_gif.gif', """It's 1337 o'clock!""")

os.remove('temp_gif.gif')
