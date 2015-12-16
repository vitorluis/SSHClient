# -*- coding: utf-8 -*-
import settings
from gi.repository import Gtk
from events.connection_window_events import ConnectionWindowEvents


class ConnectionWindow:
    glade_file = settings.APP_PATH + "/ui/connection_window.glade"
    main_object = None
    handler_class = None
    builder = None
    window = None
    refresh_list_callback = None
    connection = None

    def __init__(self, refresh_list_callback, connection=None):
        # Set some properties
        settings = Gtk.Settings.get_default()
        settings.props.gtk_button_images = True
        self.refresh_list_callback = refresh_list_callback
        self.connection = connection

        # Build the Window
        self.build_window()

        # Connect the signals
        self.connect_events()

    def build_window(self):
        # Get the builder
        self.builder = Gtk.Builder()

        # inflate the layout
        self.builder.add_from_file(self.glade_file)

        self.window = self.builder.get_object("new_connection_window")

        # If connection is not None, is an Edit, so, change the Title
        if self.connection is not None:
            self.window.set_title("Edit Connection - SSHClient")

        # Build the Tunnels table
        self.build_tunnels_table()

        self.window.show_all()

    def connect_events(self):
        # Connect the signals
        self.handler_class = ConnectionWindowEvents(self.window, self.builder, self.refresh_list_callback, self.connection)
        self.builder.connect_signals(self.handler_class)

    def build_tunnels_table(self):
        # Get the treeview from builder
        table = self.builder.get_object('tunnels_table')

        # Column Property
        column = Gtk.TreeViewColumn('Local Port', Gtk.CellRendererText(), text=0)
        column.set_clickable(False)
        column.set_resizable(True)

        # Add the column
        table.append_column(column)

        # Column Value
        column = Gtk.TreeViewColumn('Host', Gtk.CellRendererText(), text=1)
        column.set_clickable(False)
        column.set_resizable(True)
        column.set_min_width(160)

        # Add the column
        table.append_column(column)

        # Column Value
        column = Gtk.TreeViewColumn('Remote Port', Gtk.CellRendererText(), text=2)
        column.set_clickable(False)
        column.set_resizable(True)

        # Add the column
        table.append_column(column)
