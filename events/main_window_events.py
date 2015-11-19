# -*- coding: utf-8 -*-


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

        # Loop by all connections
        for connection in self.connections.get_connections():

            # Check if is the same ID
            if connection.id == connection_id:
                # Get the treeview and set the model
                table = self.builder.get_object('connections_info_tree')
                table.set_model(connection.get_model())

    def on_btn_new_connection_clicked(self, btn):
        pass

    def on_btn_edit_connection_clicked(self, btn):
        pass

    def on_btn_delete_connection_clicked(self, btn):
        pass

    def on_btn_connect_clicked(self, btn):
        pass

    def on_btn_about_clicked(self, btn):
        pass

    def on_btn_settings_clicked(self, btn):
        pass
