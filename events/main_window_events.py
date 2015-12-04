# -*- coding: utf-8 -*-
from windows.connection_window import ConnectionWindow
from model.connection import Connection
from windows.delete_connection_window import DeleteConnectionWindow


class MainWindowEvents:

    window = None
    builder = None
    connections = None

    def __init__(self, window, builder, connections):
        # Copy the parameters
        self.window = window
        self.builder = builder
        self.connections = connections

    def on_connections_tree_cursor_changed(self, tree):
        (model, treeiter) = tree.get_selection().get_selected_rows()

        # Get the connection ID
        if model is not None and len(treeiter) > 0:
            connection_id = model[treeiter][1]

            # Loop by all connections
            for connection in self.connections.get_connections():

                # Check if is the same ID
                if connection.id == connection_id:
                    # Get the treeview and set the model
                    table = self.builder.get_object('connections_info_table')
                    table.set_model(connection.get_model())

    def on_btn_edit_clicked(self, btn):
        # Get the ID of selected Connection
        tree = self.builder.get_object("connections_tree")

        # Get the selection
        (model, treeiter) = tree.get_selection().get_selected_rows()

        # Get the connection ID
        if model is not None and len(treeiter) > 0:
            # Get the ID
            connection_id = model[treeiter][1]

            # Load the Connection
            connection = Connection()
            connection.id = connection_id
            connection.load()
            connection.load_tunnels()

            # Open the Window with the connection
            ConnectionWindow(self.refresh_connections_list, connection)

    def on_btn_delete_clicked(self, btn):
        # Get the selected ID
        tree = self.builder.get_object("connections_tree")

        # Get the selection
        (model, treeiter) = tree.get_selection().get_selected_rows()

        # Get the connection ID
        if model is not None and len(treeiter) > 0:
            # Get the ID
            connection_id = model[treeiter][1]

            # Instance the dialog of delete
            DeleteConnectionWindow(connection_id, self.refresh_connections_list)

    def on_btn_connect_clicked(self, btn):
        pass

    def on_btn_refresh_clicked(self, btn):
        # Refresh the list
        self.refresh_connections_list()

    def on_new_connection_item_activate(self, item):
        # Create the Window
        ConnectionWindow(self.refresh_connections_list)

    def refresh_connections_list(self):
        # Reload the connections
        self.connections.load_connections()

        # Get the treeview
        connection = self.builder.get_object('connections_tree')
        connections_info_table = self.builder.get_object('connections_info_table')

        # Get the model and clear the list
        model = connection.get_model()
        model.clear()

        # Set the new Model
        connection.set_model(self.connections.get_connection_names_model())

        # Clear the property tables
        model = connections_info_table.get_model()
        if model is not None:
            model.clear()
