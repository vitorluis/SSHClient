# -*- coding: utf-8 -*-
from gi.repository import Gtk
from events.main_window_events import MainWindowEvents
from collection.connections import Connections


class MainWindow:
    glade_file = "ui/main_window.glade"
    main_object = None
    handler_class = None
    builder = None
    window = None
    connections = None

    def __init__(self):
        # Set some properties
        settings = Gtk.Settings.get_default()
        settings.props.gtk_button_images = True

        # On Unity, unable the system to put the menu bar on the top
        settings.props.gtk_shell_shows_menubar = False

        # Get the connections
        self.connections = Connections()
        self.connections.load_connections()

        # Build the Window
        self.build_window()

        # Connect the signals
        self.connect_events()

        # Main Loop of GTK
        Gtk.main()

    def build_window(self):
        # Get the builder
        self.builder = Gtk.Builder()

        # inflate the layout
        self.builder.add_from_file(self.glade_file)

        self.window = self.builder.get_object("main_window")
        self.window.connect("delete-event", Gtk.main_quit)

        # Build the connection TreeView
        self.build_connection_treeview()

        # Build the Connection Info talbe
        self.build_connection_info_table()

        self.window.show_all()

    def connect_events(self):
        # Connect the signals
        self.handler_class = MainWindowEvents(self.window, self.builder, self.connections)
        self.builder.connect_signals(self.handler_class)

    def build_connection_treeview(self):
        # Get the connection TreeView
        connection = self.builder.get_object('connections_tree')

        # Create the Column
        column = Gtk.TreeViewColumn('Servers', Gtk.CellRendererText(), text=0)
        column.set_clickable(False)
        column.set_resizable(True)

        # Append the column on the TreeView
        connection.append_column(column)

        # Set the model
        connection.set_model(self.connections.get_connection_names_model())

    def build_connection_info_table(self):
        # Get the treeview from builder
        table = self.builder.get_object('connections_info_table')

        # Column Property
        column = Gtk.TreeViewColumn('Property', Gtk.CellRendererText(), text=0)
        column.set_clickable(False)
        column.set_resizable(True)
        column.set_min_width(150)

        # Add the column
        table.append_column(column)

        # Column Value
        column = Gtk.TreeViewColumn('Value', Gtk.CellRendererText(), text=1)
        column.set_clickable(False)
        column.set_resizable(True)

        # Add the column
        table.append_column(column)

        # Configure the table to do not permit selection
        table.get_selection().set_mode(Gtk.SelectionMode.NONE)
