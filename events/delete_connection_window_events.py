# -*- coding: utf-8 -*-
from gi.repository import Gtk
from model.connection import Connection
from windows.message_box import MessageBox


class DeleteConnectionWindowEvents:

    window = None
    builder = None
    id_connection = None
    refresh_callback = None

    def __init__(self, window, builder, id_connection, refresh_callback):
        # Copy the parameters
        self.window = window
        self.builder = builder
        self.id_connection = id_connection
        self.refresh_callback = refresh_callback

    def on_response(self, dialog, response, user_data=None):
        if response == Gtk.ResponseType.CANCEL:
            # Just clone the Window
            self.window.destroy()
        elif response == Gtk.ResponseType.OK:
            # Call the function to delete the tunnels
            # and the connection
            self.delete_connection()

    def delete_connection(self):
        # Instance the Connection Model
        connection = Connection()
        connection.id = self.id_connection

        # Delete the tunnels
        connection.delete_tunnels()

        # Delete the connection
        if connection.delete() is False:
            MessageBox("Fail to delete the connection, please try again")
        else:
            # Call the callback
            self.refresh_callback()

            # Close the Window
            self.window.destroy()
