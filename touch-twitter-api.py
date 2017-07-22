from twitter import Twitter, OAuth

ACCESS_TOKEN = ''
ACCESS_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
t = Twitter(auth=oauth)
pythonTweets = t.search.tweets(q = "#python")
#statusUpdate = t.statuses.update(status="Hello, world!")
pythonStatuses = t.statuses.user_timeline(screen_name="elonmusk", count=5)
print pythonTweets
#print statusUpdate
print pythonStatuses