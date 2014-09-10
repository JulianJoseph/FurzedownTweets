
#!/usr/bin/python
# -*- coding: utf-8 -*-

import tweepy
import os
import ConfigParser
import inspect

# read config
config = ConfigParser.ConfigParser()
config.read("/home/pi/jules/retweet/furzedown/config")


# build savepoint path + file
lastuser = config.get("twitter","lastuser")
print lastuser

# create bot
auth = tweepy.OAuthHandler(config.get("twitter","consumer_key"), config.get("twitter","consumer_secret"))
auth.set_access_token(config.get("twitter","access_token"), config.get("twitter","access_token_secret"))
api = tweepy.API(auth)
followers = []

for follower in tweepy.Cursor(api.followers).items(25):
	followers.append(follower)

followers.reverse()
found = False

for f in followers:
	if found:
		print "New Friend!"
		print f.screen_name
		api.create_friendship(screen_name)
	if f.screen_name == lastuser:
		found = True

