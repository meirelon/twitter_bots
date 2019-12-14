import os
import pickle
from gcloud import storage
from tempfile import NamedTemporaryFile

def load_pipeline(project_id, bucket, destination_path, filename):
    client = storage.Client(project=project_id)

    with NamedTemporaryFile(mode='rb') as tempfile:
        gcs_path = os.path.join(destination_path, '{filename}.pkl'.format(filename=filename))
        client.bucket(bucket).blob(gcs_path).download_to_filename(tempfile.name)
        tempfile.seek(0)
        return pickle.load(tempfile)
