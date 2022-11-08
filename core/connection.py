from pymongo import MongoClient
from pymongo.database import Database
from core.var_env import DATABASE


class MongoConnectionProvider:
  __instance = None

  @classmethod
  def connect(cls, uri):
    """
        Establece la conexion con el servidor de mongodb y crea el connection provider
        :param uri: Cadena de conexion al servidor
        :param main_database: Nombre de la base de datos principal
        :param views_database: Nombre de la base de datos de vistas
        """
    connection = MongoClient(host=uri)
    cls.__instance = MongoConnectionProvider(connection)

  @classmethod
  def get_instance(cls):
    """
        Devuelve la instancia unica del connecion provider
        :rtype: core.connections.MongoConnectionProvider
        """
    return cls.__instance

  def __init__(self, connection):

    self.__connection = connection

  def __del__(self):
    self.__connection.close()

  def close(self):
    self.__connection.close()

  def get_database(self, database_name: str) -> Database:
    """
        Devuelve la instacia a la base de datos de vistas
        :return: Base de datos de vistas
        :rtype: pymongo.database.Database
        """
    return self.__connection.get_database(database_name)


  def get_database_views(self) -> Database:
    return self.get_database(DATABASE)