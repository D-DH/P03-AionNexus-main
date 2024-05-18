import boto3
import json
from models.artefact import Artefact
from models.tag import Tag
from models import db
from peewee import DoesNotExist
import os, signal
import uuid
import io
from PIL import Image

db.create_tables([Artefact, Tag])
account_id = os.getenv("account_name", "730335628388")
region = os.getenv("region", "us-east-1")
shutdown_signal = False

# initial sqs queue and s3 bucket
sqs = boto3.resource("sqs", region)
queue = sqs.Queue(f'https://sqs.{region}.amazonaws.com/{account_id}/artefacts')
s3 = boto3.resource("s3", region)

def get_tag_ids(tags):
    tag_ids = []
    for tag in tags:
        try:
            tag_id = Tag.get(Tag.name == tag).id
        except DoesNotExist:
            tag_id = str(uuid.uuid4())
            Tag.create(id=tag_id, name=tag, system_generated=True)
        tag_ids.append(tag_id)
    return tag_ids

def read_image_from_s3(artefact_s3_key):
    bucket = s3.Bucket("aion-nexus-artefacts")
    object = bucket.Object(artefact_s3_key)
    response = object.get()
    file_stream = response['Body']
    return Image.open(file_stream)

def scan_artefact(artefact_s3_key):
    read_image_from_s3(artefact_s3_key)
    # TODO: call ML model to scan artefact
    tags = ["painting", "canvas"]
    return tags

def process_message(message):
    artefact = json.loads(message.body)
    artefact_id = artefact['id']
    try:
        tags = scan_artefact(artefact['s3_key'])
        tag_ids = get_tag_ids(tags)
        Artefact.update({Artefact.tags:json.dumps(tag_ids)}).where(Artefact.id == artefact_id).execute()
        Artefact.update({Artefact.status:"scanned"}).where(Artefact.id == artefact_id).execute()
    except Exception as e:
        print("Error scanning artefact: ", e)
        Artefact.update({Artefact.status:"failed"}).where(Artefact.id == artefact_id).execute()
    message.delete()

def shutdown(signum, frame):
    print('Caught SIGTERM, shutting down.')
    global shutdown_signal
    shutdown_signal = True

if __name__ == "__main__":
    print("Starting new email scanner.")
    # Register handler
    signal.signal(signal.SIGTERM, shutdown)
    # Main logic goes here
    while not shutdown_signal:
        messages = queue.receive_messages(
            AttributeNames=[],
            MessageAttributeNames=[],
            MaxNumberOfMessages=10,
            WaitTimeSeconds=20,
        )
        for message in messages:
            process_message(message)
    print("Shutting down email scanner.")
    exit(0)
