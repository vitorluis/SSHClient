# -*- coding: utf-8 -*-
from data.database import DBConnection


class Settings:
    # Constants
    (X11_FORWARD, REQUEST_COMPRESSION, FORCE_IPV4, FORCE_IPV6) = (
        "x11_forward", "request_compression", "force_ipv4", "force_ipv6"
    )

    # Properties
    x11_forward = None
    request_compression = None
    force_ipv4 = None
    force_ipv6 = None

    def save(self):
        # Instance the database
        database = DBConnection()

        # Remove the settings from database
        database.execute_query("DELETE FROM settings")

        # Create the list of params
        params = [(Settings.X11_FORWARD, self.x11_forward),
                  (Settings.REQUEST_COMPRESSION, self.request_compression),
                  (Settings.FORCE_IPV4, self.force_ipv4),
                  (Settings.FORCE_IPV6, self.force_ipv6)]

        # Save the settings
        affected_rows = database.execute_query_many(
            "INSERT INTO settings (property, value) VALUES (?, ?)", params
        )

        if affected_rows == 4:
            # Saved all settings
            return True
        else:
            # Something is wrong, try again
            return False

    def load(self):
        # Create the databse
        database = DBConnection()

        # Make the select
        rows = database.select_query("SELECT * FROM settings")
        for row in rows:
            # Check the name of the property and set the value correctly
            if row['property'] == Settings.X11_FORWARD:
                self.x11_forward = int(row['value'])
            elif row['property'] == Settings.REQUEST_COMPRESSION:
                self.request_compression = int(row['value'])
            elif row['property'] == Settings.FORCE_IPV4:
                self.force_ipv4 = int(row['value'])
            elif row['property'] == Settings.FORCE_IPV6:
                self.force_ipv6 = int(row['value'])
