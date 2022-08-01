from datetime import datetime, date
from utilities.db.db_manager import dbManager


class Pizza:
    def __init__(self):
        super().__init__()
        self.cursor = None


    def getPizza(self, id):
        query = f"select * from pizza where id='%s'" % id
        query_result = dbManager.fetch(query)
        return query_result

    def getAllPizza(self):
        query = f"select * from pizza"
        query_result = dbManager.fetch(query)
        return query_result

