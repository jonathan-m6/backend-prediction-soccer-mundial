import os
from dotenv import load_dotenv

load_dotenv('.config\.env')

DATABASE = os.getenv('name_mongoDBTest')
MONGO_URI = os.getenv('mongo_uri')
EVENTS_URI = os.getenv('uri_events')

