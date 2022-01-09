"""
Sometimes you find yourself using quit voluminous files, which you can't push to github as assets
You may want to store and download them in the runtime Or only when you need them
usualy I do that using google storege buckets
You can put the code of the download here and run the file when you create the docker image
If the file are multiple gigabyte you might consider running a kubernetes job to donload the files 
into a kubenete persistent volume 
and them make the volume accessible by all the pods in need 
"""
from google.cloud import storage
import logging
from logging.config import fileConfig

fileConfig('./logging_config_stream.ini')
logger = logging.getLogger()

storage_client = storage.Client.from_service_account_json("key_path.json")
bucket = storage_client.get_bucket("bucket-name")
blobs = list(bucket.list_blobs(prefix='directory-in-the-bucket/'))
for blob in blobs: 
    blob.download_to_filename(f'folder_path/{blob.name}')