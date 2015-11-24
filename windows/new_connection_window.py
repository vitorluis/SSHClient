# -*- coding: utf-8 -*-
from gi.repository import Gtk
from events.new_connection_window_events import NewConnectionWindowEvents


class NewConnectionWindow:
    glade_file = "ui/new_connection_window.glade"
    main_object = None
    handler_class = None
    builder = None
    window = None
    refresh_list_callback = None

    def __init__(self, refresh_list_callback):
        # Set some properties
        settings = Gtk.Settings.get_default()
        settings.props.gtk_button_images = True
        self.refresh_list_callback = refresh_list_callback

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

        # Build the Tunnels table
        self.build_tunnels_table()

        self.window.show_all()

    def connect_events(self):
        # Connect the signals
        self.handler_class = NewConnectionWindowEvents(self.window, self.builder, self.refresh_list_callback)
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

        # Add the column
        table.append_column(column)

        # Column Value
        column = Gtk.TreeViewColumn('Remote Port', Gtk.CellRendererText(), text=1)
        column.set_clickable(False)
        column.set_resizable(True)

        # Add the column
        table.append_column(column)
