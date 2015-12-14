# -*- coding: utf-8 -*-
from data.database import DBConnection


class Settings:
    # Constants
    (X11_FORWARD, REQUEST_COMPRESSION, FORCE_IPV4, FORCE_IPV6) = (
        "x11_forward", "compress_request", "force_ipv4", "force_ipv6"
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

        # Save the settings
        # X11 Forward
        database.execute_query(
            "INSERT INTO settings (property, value) VALUES ('{}', {})".format(Settings.X11_FORWARD, self.x11_forward)
        )

        # Compression
        database.execute_query(
            "INSERT INTO settings (property, value) VALUES ('{}', {})".format(Settings.REQUEST_COMPRESSION, self.request_compression)
        )

        # Force IPv4
        database.execute_query(
            "INSERT INTO settings (property, value) VALUES ('{}', {})".format(Settings.FORCE_IPV4, self.force_ipv4)
        )

        # Force IPv6
        database.execute_query(
            "INSERT INTO settings (property, value) VALUES ('{}', {})".format(Settings.FORCE_IPV6, self.force_ipv6)
        )

    def load(self):
        # Create the databse
        database = DBConnection()

        # Make the select
        results = database.select_query("SELECT * FROM settings")
