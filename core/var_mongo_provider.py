from core.connection import MongoConnectionProvider
import core.var_env as variables

MongoConnectionProvider.connect(variables.env["mongo_uri"])
db=MongoConnectionProvider.get_instance().get_database_views()