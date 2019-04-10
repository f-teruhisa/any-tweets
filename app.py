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

@app.route('/', methods=["GET", "POST"])
def index():
   if request.method == 'POST':
       user_id = request.form['user_id']
       tweets_df = get_tweets_df(user_id)
       grouped_df = get_grouped_df(tweets_df)
       sorted_df = get_sorted_df(tweets_df)
       return render_template(
           'index.html',
           profile=get_profile(user_id),
           tweets_df=tweets_df,
           grouped_df=grouped_df,
           sorted_df=sorted_df
       )
   else:
       return render_template('index.html')


app.run(host="localhost")
