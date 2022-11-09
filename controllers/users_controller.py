from fastapi import APIRouter, status, HTTPException
from models.user import user
import core.var_mongo_provider as mongo_provider
import shortuuid

router = APIRouter(
  prefix="/user",
  tags=["Usuario"],
  responses={404: {"description": "Not found"}},
)

@router.post("", status_code=status.HTTP_201_CREATED)
async def user_post(contract: user):
  user=mongo_provider.db.users.find_one({'username':contract.username})
  if not user:
    user ={**contract.dict(), '_id': shortuuid.uuid()}
    mongo_provider.db.users.insert_one(user)
  elif not (user['username']==contract.username and user['email']==contract.email):
    raise HTTPException(409,"Usuario ya existe")
  return user

@router.post("/{id_usuario}/amigo", status_code=status.HTTP_201_CREATED)
async def user_put(id_usuario:str, body: dict):
  friend=mongo_provider.db.users.find_one({'username': body['username']})
  if not friend:
    raise HTTPException(409,"Usuario no existente")
  
  user=mongo_provider.db.users.find_one({'_id': id_usuario})
  user['amigos'].append(friend['username'])

  mongo_provider.db.users.update_one({'_id': id_usuario}, {'$set': user})
  return user

@router.get("/{id_usuario}/table", status_code=status.HTTP_201_CREATED)
async def table_get(id_usuario:str, body: dict):
  user = mongo_provider.db.users.find_one({'_id': id_usuario})
  arrayTable = user['amigos']
  arrayTable.append(user['username'])

  users = mongo_provider.db.users.find({'username': {'$in': arrayTable}}).sort({'total': -1})
  return users