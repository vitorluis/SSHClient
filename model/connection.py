# -*- coding: utf-8 -*-
from pprint import pprint
from gi.repository import Gtk
from data.database import DBConnection
from collection.tunnels import Tunnels
from model.tunnel import Tunnel


class Connection:

    id = None
    name = None
    host = None
    port = None
    user = None
    password = None
    use_key = False
    key_path = None
    tunnels = None
    model = None

    def __init__(self):
        self.tunnels = Tunnels()

    def load(self):
        # Create the DBConnection
        database = DBConnection()

        # Create the SQL
        sql = "select * from connections where id_connection = {}"

        # Bind the value
        sql = sql.format(self.id)

        # Execute the query
        rows = database.select_query(sql)

        # Set the attrs
        for row in rows:
            self.name = row['name']
            self.host = row['host']
            self.port = row['port']
            self.user = row['user']
            self.password = row['passwd']
            self.use_key = True if int(row['use_key']) == 1 else False
            self.key_path = row['key_path']

    def load_tunnels(self):
        # Clear the tunnels list form the collection
        self.tunnels.clear_tunnels()

        # Create the DBConnection
        database = DBConnection()

        # Create the SQL
        sql = "select * from tunnels where id_connection = {}"

        # Bind the value
        sql = sql.format(self.id)

        # Execute the query
        rows = database.select_query(sql)

        # Set the attrs
        for row in rows:
            tunnel = Tunnel()
            tunnel.id = row['id_tunnel']
            tunnel.id_connection = self.id
            tunnel.local_port = row['local_port']
            tunnel.address = row['address']
            tunnel.remote_port = row['remote_port']

            # Add on Tunnels
            self.tunnels.add_tunnel(tunnel)

    def save(self):
        # Create the DBConnection
        database = DBConnection()

        # Create the SQL
        if self.id is None:
            sql = "INSERT INTO connections (name, host, port, user, passwd, use_key, key_path)" \
                " VALUES ('{}', '{}', {}, '{}', '{}', {}, '{}');"
        else:
            sql = "UPDATE connections SET name = '{}', host = '{}', port = {}, user = '{}', passwd = '{}'," \
                  " use_key = {}, key_path = '{}' where id_connection = {}"

        # Bind the values
        sql = sql.format(
            self.name,
            self.host,
            self.port,
            self.user,
            self.password,
            1 if self.use_key else 0,
            self.key_path,
            self.id
        )

        # Execute the SQL
        if database.execute_query(sql) > 0:
            # Get the last row inserted
            if self.id is None:
                self.id = database.cursor.lastrowid

            # Return true telling it's OK
            return True
        else:
            # Return False for fail
            return False

    def get_tunnels(self):
        return self.tunnels

    def delete_tunnels(self):
        # Check if have the connection ID
        if self.id is not None:
            # Create the DBConnection
            database = DBConnection()

            # Create the SQL
            sql = "delete from tunnels where id_connection = {}"

            # Bind the value
            sql = sql.format(self.id)

            # Execute the query
            if database.execute_query(sql) > 0:
                # Return true telling it's OK
                return True
            else:
                # Return False
                return False

    def delete(self):
        # Check if have the connection ID
        if self.id is not None:
            # Create the DBConnection
            database = DBConnection()

            # Create the SQL
            sql = "delete from connections where id_connection = {}"

            # Bind the value
            sql = sql.format(self.id)

            # Execute the query
            if database.execute_query(sql) > 0:
                # Return true telling it's OK
                return True
            else:
                # Return False
                return False

    def get_model(self):
        # Create the Model
        self.model = Gtk.ListStore(str, str)
        self.model.append(["Name", self.name])
        self.model.append(["Host", self.host])
        self.model.append(["Port", str(self.port)])
        self.model.append(["User", self.user])
        self.model.append(["Use Key", "Yes" if self.use_key else "No"])
        self.model.append(["Key Path", self.key_path])

        # Return the Model
        return self.model

    def generate_ssh_command(self):
        # Get the settings
        # Check if uses key
        if self.use_key is True:
            command = "/usr/bin/ssh {}@{} -i {}"
            command = command.format(self.user, self.host, self.key_path)
        else:
            command = "/usr/bin/sshpass -p{} /usr/bin/ssh {}@{}"
            command = command.format(self.password, self.user, self.host)

        # Format other parameters
        command += " -p {}"
        command = command.format(self.port)

        # Get the tunnels
        for tunnel in self.tunnels.get_tunnels():
            command += " -L {}:{}:{}"
            command = command.format(tunnel.local_port, tunnel.address, tunnel.remote_port)

        # At the end, return the command
        return command
