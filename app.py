import tweepy
import pandas as pd
from flask import Flask, render_template, request, logging, Response, redirect, flash
from config import CONFIG

# Set the Twitter's Key
CONSUMER_KEY = CONFIG["CONSUMER_KEY"]
CONSUMER_SECRET = CONFIG["CONSUMER_SECRET"]
ACCESS_TOKEN = CONFIG["ACCESS_TOKEN"]
ACCESS_SECRET = CONFIG["ACCESS_SECRET"]

# Tweepy auth
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# Generate API instace
api = tweepy.API(auth)

app = Flask(__name__)


# Twitter datas
columns = [
    "tweet_id",
    "created_at",
    "text",
    "fav",
    "retweets"
]

@app.route('/', methods = ["GET" , "POST"])
def index():
   if request.method == 'POST':
       # Get name = "user_id" on form
       user_id = request.form['user_id']
       return render_template('index.html', user_id = user_id)
   else:
       return render_template('index.html')


app.run(host="localhost")
