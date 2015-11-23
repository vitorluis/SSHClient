# -*- coding: utf-8 -*-
from gi.repository import Gtk
from data.database import DBConnection


class Connection:

    id = None
    name = None
    host = None
    port = None
    user = None
    password = None
    use_key = False
    key_path = None
    model = None

    def __init__(self):
        pass

    def save(self):
        # Create the DBConnection
        database = DBConnection()

        # Create the SQL
        sql = ""

        # Execute the SQL
        if database.execute_query(sql) > 0:
            return True
        else:
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
