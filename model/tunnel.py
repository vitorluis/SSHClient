# -*- coding: utf-8 -*-
from data.database import DBConnection


class Tunnel:

    id = None
    id_connection = None
    local_port = None
    address = None
    remote_port = None

    def __init__(self):
        pass

    def save(self):
        # Create the DBConnection
        database = DBConnection()

        # Create the SQL
        sql = "INSERT INTO tunnels (id_connection, local_port, address, remote_port)" \
              " VALUES ({}, {}, '{}', {});"

        # Bind the values
        sql = sql.format(self.id_connection, self.local_port, self.address, self.remote_port)

        # Execute the SQL
        if database.execute_query(sql) > 0:
            # Get the last row inserted
            self.id = database.cursor.lastrowid

            # Return true telling it's OK
            return True
        else:
            # Return False for fail
            return False
        pass
