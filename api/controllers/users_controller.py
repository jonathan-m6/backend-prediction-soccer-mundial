import shortuuid
from fastapi import APIRouter, status, HTTPException
import core.var_mongo_provider as mongo_provider
from api.models.user import user

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