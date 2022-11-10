from service_event import *
from core.var_env import EVENTS_URI
import core.var_mongo_provider as mongo_provider
import requests

""" MongoConnectionProvider.connect(variables.env["mongo_uri"])

db=MongoConnectionProvider.get_instance().get_database_views() """


data=requests.get(EVENTS_URI).json()

list_events=[]
for item in data["events"]:
    contract=get_contract(item)
    contract['nombreLocal'], contract['nombreVisita'], contract['isoLocal'], contract['isoVisita'], contract['versus'] = find_countries(contract['equipoLocal'], contract['equipoVisita'])
    query={'_id':contract['_id']}
    update={'$set':contract}
    list_events.append(contract)
    mongo_provider.db.events.update_one(query,update,True)

print("Eventos cargados")