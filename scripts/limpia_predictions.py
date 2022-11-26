from datetime import date, datetime, time
from dateutil.parser import parse
import core.var_mongo_provider as mongo_provider



users = list(mongo_provider.db.users.find({}))

repetidos = list()
for user in users:
  predictions = list(mongo_provider.db.predictions.find({'userId': user['_id']}))
  eventIds = list()
  for prediction in predictions:
    if prediction['eventId'] in eventIds:
      repetidos.append(prediction)
    else:
      eventIds.append(prediction['eventId'])



print(repetidos)