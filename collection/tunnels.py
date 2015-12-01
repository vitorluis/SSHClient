# -*- coding: utf-8 -*-
from data.database import DBConnection
from model.tunnel import Tunnel
from gi.repository import Gtk


class Tunnels:

    dbconnection = None
    tunnels = []
    model = None

    def __init__(self):
        # Create the DB connection
        self.dbconnection = DBConnection()

    def add_tunnel(self, tunnel):
        self.tunnels.append(tunnel)

    def load_tunnels(self):
        # Reset the List
        self.tunnels = []

        # Create the SQL
        sql = "select * from tunnels order by name"

        # Execute the sql
        results = self.dbconnection.select_query(sql)

        # Create a model for every tunnel
        for row in results:
            # Create new Connection
            tunnel = Tunnel()
            tunnel.id = row['id_tunnel']
            tunnel.id_connection = row['id_connection']
            tunnel.local_port = row['local_port']
            tunnel.address = row['address']
            tunnel.remote_port = row['remote_port']

            # Add to the list
            self.tunnels.append(tunnel)

    # Method to get ListStore of names
    def get_tunnels_model(self):
        # Create the ListStore
        self.model = Gtk.ListStore(int, str, int)

        # Looping passing by every tunnel
        for tunnel in self.tunnels:
            self.model.append([int(tunnel.local_port), tunnel.address, int(tunnel.remote_port)])

        # return the model
        return self.model

    # Return all Connection
    def get_tunnels(self):
        return self.tunnels
