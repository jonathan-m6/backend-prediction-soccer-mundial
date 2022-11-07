from service_event import *
from core.connection import MongoConnectionProvider
import core.var_env as variables
import requests

MongoConnectionProvider.connect(variables.env["mongo_uri"])

db=MongoConnectionProvider.get_instance().get_database_views()


data=requests.get(variables.env['uri_events']).json()

list_events=[]
for item in data["events"]:
    contract=get_contract(item)
    query={'idEvent':contract['idEvent']}
    update={'$set':contract}
    db.games_events.update_one(query,update,True)
    db.games_events.update_many()

print(list_events)