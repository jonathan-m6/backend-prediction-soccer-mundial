from fastapi import APIRouter
import core.var_mongo_provider as mongo_provider
from scripts.service_event import get_contract, find_countries
from core.var_env import EVENTS_URI
import requests
from datetime import date, datetime, time
from dateutil.parser import parse

router = APIRouter(
    prefix="/utils",
    tags=["Utils"],
    responses={404: {"description": "Not found"}},
)

@router.get("/update")
async def get_update_events():
  data=requests.get(EVENTS_URI).json()
  list_events=[]
  for item in data["events"]:
    contract=get_contract(item)
    contract['nombreLocal'], contract['nombreVisita'], contract['isoLocal'], contract['isoVisita'], contract['versus'] = find_countries(contract['equipoLocal'], contract['equipoVisita'])
    query={'_id':contract['_id']}
    update={'$set':contract}
    list_events.append(contract)
    mongo_provider.db.events.update_one(query,update,True)
  return "Update done"
    
@router.get("/multiple")
async def get_multiple_predictions():
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
  return {"total":len(repetidos), "repetidos":repetidos}

@router.get("/count")
async def get_count_points():
  date_start,date_end=get_date_range()
  query = { 
    '$and': [
      {'fechaOrder': {'$gte':  date_start}},
      {'fechaOrder': {'$lte': date_end}}
    ]
  }
  list_events = list(mongo_provider.db.events.find(query))

  perfects_predictions = list()
  good_predictions = list()

  for event in list_events:
      prediction_list = list(mongo_provider.db.predictions.find({'eventId': event['_id']}))
      event_winner = who_win(event['golesLocal'], event['golesVisita'])
      
      for prediction in prediction_list:
        prediction_winner = who_win(prediction['golesLocal'], prediction['golesVisita'])
        if prediction_winner == event_winner:
          if prediction['golesVisita'] == event['golesVisita'] and prediction["golesLocal"] == event["golesLocal"]:
            perfects_predictions.append(prediction)
          else: good_predictions.append(prediction)

  users = list()

  for pp in perfects_predictions:
    index = indexOf(pp["userId"], users)
    if index == -1:
      entity = mongo_provider.db.users.find_one({'_id': pp['userId']})
      if entity:
        entity["puntosMarcador"] += 1
        entity["puntosResultado"] += 1
        entity["total"] += 2
        users.append(entity)
    else:
      users[index]["puntosMarcador"] += 1
      users[index]["puntosResultado"] += 1
      users[index]["total"] += 2

  for gp in good_predictions:
    index = indexOf(gp["userId"], users)
    if index == -1:
      entity = mongo_provider.db.users.find_one({'_id': gp['userId']})
      if entity:
        entity["puntosResultado"] += 1
        entity["total"] += 1
        users.append(entity)
    else:
      users[index]["puntosResultado"] += 1
      users[index]["total"] += 1

  for user in users:
    mongo_provider.db.users.update_one({"_id": user["_id"]}, {'$set': user})
  return 'calculation done'

def who_win(local, visita):
  winner = 'empate'
  if local > visita:
    winner = 'local'
  elif visita > local:
    winner = 'visita'
  return winner

def indexOf(userId, users):
  index = -1
  try:
    index = [x["_id"] for x in users ].index(userId)
  except ValueError:
    index = -1
  return index

def get_date_range():
  start = date.today()
  end = date.today()

  min_date_time = datetime.combine(start, time.min)
  max_date_time = datetime.combine(end, time.max)
  return min_date_time, max_date_time