import os
import pickle
from gcloud import storage
from tempfile import NamedTemporaryFile
import tweepy

def load_pipeline(project_id, bucket, destination_path, filename):
    client = storage.Client(project=project_id)

    with NamedTemporaryFile(mode='rb') as tempfile:
        gcs_path = os.path.join(destination_path, '{filename}.pkl'.format(filename=filename))
        client.bucket(bucket).blob(gcs_path).download_to_filename(tempfile.name)
        tempfile.seek(0)
        return pickle.load(tempfile)


class twitterApi:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.consumer_key=consumer_key
        self.consumer_secret=consumer_secret
        self.access_token=access_token
        self.access_token_secret=access_token_secret


    def twitter_auth(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        return tweepy.API(auth)
