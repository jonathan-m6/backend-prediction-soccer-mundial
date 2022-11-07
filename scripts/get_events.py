from service_event import *
from core.connection import MongoConnectionProvider
import core.var_env as variables
import core.var_mongo_provider as mongo_provider
import requests

""" MongoConnectionProvider.connect(variables.env["mongo_uri"])

db=MongoConnectionProvider.get_instance().get_database_views() """


data=requests.get(variables.env['uri_events']).json()

list_events=[]
for item in data["events"]:
    contract=get_contract(item)
    query={'_id':contract['_id']}
    update={'$set':contract}
    list_events.append(contract)
    mongo_provider.db.events.update_one(query,update,True)

print("Eventos cargados")