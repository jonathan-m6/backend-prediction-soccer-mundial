from core.connection import MongoConnectionProvider
from dotenv import dotenv_values

env=dotenv_values(".config\.env")

MongoConnectionProvider.connect(env["mongo_uri"])
db=MongoConnectionProvider.get_instance().get_database_views()