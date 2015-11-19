# -*- coding: utf-8 -*-
from data.database import DBConnection
from model.connection import Connection
from gi.repository import Gtk


class Connections:

    dbconnection = None
    connections = []
    model = None

    def __init__(self):
        # Create the DB connection
        self.dbconnection = DBConnection()

    def load_connections(self):
        # Create the SQL
        sql = "select * from connections"

        # Execute the sql
        results = self.dbconnection.select_query(sql)

        # Create a model for every connection
        for row in results:
            # Create new Connection
            connection = Connection()
            connection.id = row['id_connection']
            connection.name = row['name']
            connection.host = row['host']
            connection.user = row['user']
            connection.port = row['port']
            connection.use_key = True if row['use_key'] == 1 else False
            connection.key_path = row['key_path']

            # Add to the list
            self.connections.append(connection)

    # Method to get ListStore of names
    def get_connection_names_model(self):
        # Create the ListStore
        self.model = Gtk.ListStore(str, int)

        # Looping passing by every connection
        for connection in self.connections:
            self.model.append([connection.name, connection.id])

        # return the model
        return self.model

    # Return all Connection
    def get_connections(self):
        return self.connections
