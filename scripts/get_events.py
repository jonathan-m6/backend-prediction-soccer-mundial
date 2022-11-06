from service_event import *
from core.connection import MongoConnectionProvider
from core.var_env import env
import requests

MongoConnectionProvider.connect(env["mongo_uri"])

db=MongoConnectionProvider.get_instance().get_database_views()


data=requests.get(env['uri_events']).json()

list_events=[]
for item in data["events"]:
    contract=get_contract(item)
    query={'idEvent':contract['idEvent']}
    update={'$set':contract}
    db.games_events.update_one(query,update,True)

print(list_events)