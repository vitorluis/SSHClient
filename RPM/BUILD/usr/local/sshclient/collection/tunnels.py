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
        # Add to the list
        self.tunnels.append(tunnel)

    def remove_tunnel_at(self, index):
        # Remove the tunnel
        if len(self.tunnels) > 0:
            self.tunnels.pop(index)

    def load_tunnels(self, id_connection):
        # Reset the List
        self.tunnels = []

        # Create the SQL
        sql = "select * from tunnels where id_connection = {}"
        sql = sql.format(id_connection)

        # Execute the sql
        results = self.dbconnection.select_query(sql)

        # Create a model for every tunnel
        for row in results:
            # Create new Connection
            tunnel = Tunnel()
            tunnel.id = 0 if row['id_tunnel'] is None else row['id_tunnel']
            tunnel.id_connection = 0 if row['id_connection'] is None else row['id_connection']
            tunnel.local_port = row['local_port']
            tunnel.address = row['address']
            tunnel.remote_port = row['remote_port']

            # Add to the list
            self.tunnels.append(tunnel)

    def clear_tunnels(self):
        # Clear list of tunnels
        self.tunnels = []

    # Method to get ListStore of names
    def get_tunnels_model(self):
        # Create the ListStore
        self.model = Gtk.ListStore(int, str, int, int)

        # Looping passing by every tunnel
        index = 0
        for tunnel in self.tunnels:
            # Add the model
            self.model.append([int(tunnel.local_port), tunnel.address, int(tunnel.remote_port), index])

            # Increment the counter
            index += 1

        # return the model
        return self.model

    # Return all Connection
    def get_tunnels(self):
        return self.tunnels
