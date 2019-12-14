import os
import pickle
from datetime import datetime
from gcloud import storage
from tempfile import NamedTemporaryFile

from deps.utils import load_pipeline



def bernie_tweet(request):
    project = os.environ["PROJECT_ID"]
    bucket = os.environ["BUCKET"]
    destination_path = os.environ["DESTINATION_PATH"]
    filename = os.environ["FILENAME"]

    bot = load_pipeline(project_id=project,
                        bucket=bucket,
                        destination_path=destination_path,
                        filename=filename)

    return bot.make_short_sentence(140)
