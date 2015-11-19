# -*- coding: utf-8 -*-
from pprint import pprint


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
        connection_id = model[treeiter][1]

        # Load the properties of this connection
