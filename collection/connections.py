# -*- coding: utf-8 -*-
from data.database import DBConnection
from pprint import pprint


class Connections:

    dbconnection = None
    connections = []

    def __init__(self):
        # Create the DB connection
        self.dbconnection = DBConnection()

    def load_connections(self):
        # Create the SQL
        sql = "select * from connections"

        # Execute the sql
        results = self.dbconnection.select_query(sql)
        pprint(results)
