from fastapi import APIRouter, status, HTTPException
from models.user import user
import core.var_mongo_provider as mongo_provider
import shortuuid

router = APIRouter(
  prefix="/user",
  tags=["Usuario"],
  responses={404: {"description": "Not found"}},
)

@router.post("")
async def user_post(contract: user):
  userNameContract=contract.username.lower().replace(" ","")
  user=mongo_provider.db.users.find_one({'username':userNameContract})
  if not user:
    user ={**contract.dict(), '_id': shortuuid.uuid()}
    user['username'] = userNameContract
    user['email'] = user['email'].lower()
    mongo_provider.db.users.insert_one(user)
  elif not (user['username'].lower()==userNameContract and user['email'].lower()==contract.email.lower()):
    raise HTTPException(409,"Usuario ya existe")
  return user

@router.put("/{id_usuario}/amigo")
async def user_put(id_usuario:str, body: dict):
  friend=mongo_provider.db.users.find_one({'username': body['username'].lower().replace(" ","")})
  user=mongo_provider.db.users.find_one({'_id': id_usuario})
  if not 'amigos' in user:
    user["amigos"]=[]
  if friend["username"]==user["username"] or friend["username"] in user["amigos"]:
    raise HTTPException(403,"Usuario no valido")

  if not friend:
    raise HTTPException(409,"Usuario no existente")
  
  user['amigos'].append(friend['username'])

  mongo_provider.db.users.update_one({'_id': id_usuario}, {'$set': user})
  return user

@router.get("/{id_usuario}/table")
async def table_get(id_usuario:str):
  user = mongo_provider.db.users.find_one({'_id': id_usuario})
  arrayTable = user['amigos'] if 'amigos' in user else []
  arrayTable.append(user['username'])

  users = mongo_provider.db.users.find({'username': {'$in': arrayTable}}).sort("total",-1)
  return list(users)


@router.delete("/{id_usuario}/delete")
async def user_delete(id_usuario:str):
  mongo_provider.db.users.delete_one({'_id': id_usuario})
  return {'message': 'ok'}