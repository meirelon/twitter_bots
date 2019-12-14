import os
import pickle
import requests
from datetime import datetime
from gcloud import storage
from tempfile import NamedTemporaryFile

from deps.utils import load_pipeline
from deps.utils import twitterApi



def bernie_tweet(request):
    project = os.environ["PROJECT_ID"]
    bucket = os.environ["BUCKET"]
    destination_path = os.environ["DESTINATION_PATH"]
    filename = os.environ["FILENAME"]

    bot = load_pipeline(project_id=project,
                        bucket=bucket,
                        destination_path=destination_path,
                        filename=filename)

    try:
        tweet = bot.make_short_sentence(140)
    except:
        tweet = ""

    return tweet


def tweet_send(request):
    #gcp
    project = os.environ["PROJECT_ID"]
    #twitter
    consumer_key = os.environ["CONSUMER_KEY"]
    consumer_secret = os.environ["CONSUMER_SECRET"]
    access_token = os.environ["ACCESS_TOKEN"]
    access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]
    tweet_type = os.environ["TWEET_TYPE"]

    twitter = twitterApi(consumer_key=consumer_key,
                     consumer_secret=consumer_secret,
                     access_token=access_token,
                     access_token_secret=access_token_secret)

    api = twitter.twitter_auth()

    r = requests.get("https://us-central1-{project}.cloudfunctions.net/{tweet_type}".format(project=project, tweet_type=tweet_type))
    api.update_status(r.text)
    # update status
    return "success"
