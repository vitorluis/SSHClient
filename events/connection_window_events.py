# -*- coding: utf-8 -*-
from windows.message_box import MessageBox
from model.connection import Connection
from windows.new_tunnel_window import NewTunnelWindow
from collection.tunnels import Tunnels


class ConnectionWindowEvents:

    window = None
    builder = None
    refresh_list_callback = None
    tunnels = None
    index_to_remove = None
    connection = None

    def __init__(self, window, builder, refresh_list_callback, connection=None):
        # Copy the parameters
        self.window = window
        self.builder = builder
        self.refresh_list_callback = refresh_list_callback
        self.tunnels = Tunnels()

        # If id_connection is not None, load the connection to Edit
        if connection is not None:
            self.connection = connection
            self.load_connection()

        # Connect the event notify::active of the switch key
        switch = self.builder.get_object("switch_use_key")
        switch.connect("notify::active", self.on_switch_use_key_activate)

    def on_switch_use_key_activate(self, switch, active):
        # Get the password fields
        password = self.builder.get_object("txt_password")
        confirm_password = self.builder.get_object("txt_password_confirm")
        file_chooser = self.builder.get_object("filechooser_key")

        if switch.get_active():
            # Disable them
            password.set_sensitive(False)
            confirm_password.set_sensitive(False)
            file_chooser.set_sensitive(True)
        else:
            # Enable them
            password.set_sensitive(True)
            confirm_password.set_sensitive(True)
            file_chooser.set_sensitive(False)

    def on_btn_add_clicked(self, btn):
        NewTunnelWindow(self.on_added_tunnel_callback)

    def on_tunnels_table_cursor_changed(self, treeview):
        # Get the Index
        (model, path) = treeview.get_selection().get_selected()
        if model is not None and path is not None:
            self.index_to_remove = model[path][3]

    def on_added_tunnel_callback(self, tunnel):
        # Add the tunnel on the list
        self.tunnels.add_tunnel(tunnel)

        # Add to the table the new model
        table = self.builder.get_object("tunnels_table")

        # Get and clean the model
        model = table.get_model()
        if model is not None:
            model.clear()

        # Set the new model
        table.set_model(self.tunnels.get_tunnels_model())

    def on_btn_remove_clicked(self, btn):
        # Remove the line tunnel from the collection and rebuild the table
        self.tunnels.remove_tunnel_at(self.index_to_remove)

        # Rebuild the table
        table = self.builder.get_object("tunnels_table")

        # Get and clean the model
        model = table.get_model()
        if model is not None:
            model.clear()

        # Set the new model
        table.set_model(self.tunnels.get_tunnels_model())

    def on_btn_save_clicked(self, btn):
        # First of all, validate the form
        if self.validate_form():
            # If OK, save the connection
            if self.save_connection():
                # Run the callback
                if self.refresh_list_callback is not None:
                    # Call the callback to refresh the connection list
                    self.refresh_list_callback()

                # Close the Window
                self.window.destroy()
            else:
                # Show a message Box telling the save fails
                MessageBox("Fail to save the connection. Check if have duplicate names. Try again")

    def on_btn_cancel_clicked(self, btn):
        self.window.destroy()

    def load_connection(self):
        # Get all objects
        name = self.builder.get_object("txt_name")
        host = self.builder.get_object("txt_host")
        port = self.builder.get_object("txt_port")
        user = self.builder.get_object("txt_user")
        switch_key = self.builder.get_object("switch_use_key")
        password = self.builder.get_object("txt_password")
        confirm_password = self.builder.get_object("txt_password_confirm")
        file_chooser = self.builder.get_object("filechooser_key")
        table = self.builder.get_object("tunnels_table")

        # Set the values
        name.set_text(self.connection.name)
        host.set_text(self.connection.host)
        port.set_text(str(self.connection.port))
        user.set_text(self.connection.user)
        switch_key.set_active(self.connection.use_key)
        password.set_text(self.connection.password)
        confirm_password.set_text(self.connection.password)

        if self.connection.key_path != 'None':  # On SQLITE is saved as str 'None'
            file_chooser.set_filename(self.connection.key_path)

        # Check if use key is checked, and call the function to switch the fields
        if self.connection.use_key:
            self.on_switch_use_key_activate(switch_key, self.connection.use_key)

        # Also, load the tunnels
        self.tunnels = self.connection.get_tunnels()

        # Get and clean the model
        model = table.get_model()
        if model is not None:
            model.clear()

        # Set the new model
        table.set_model(self.tunnels.get_tunnels_model())

    def validate_form(self):
        # Get all object that need be validated
        name = self.builder.get_object("txt_name")
        host = self.builder.get_object("txt_host")
        port = self.builder.get_object("txt_port")
        user = self.builder.get_object("txt_user")
        switch_key = self.builder.get_object("switch_use_key")
        password = self.builder.get_object("txt_password")
        confirm_password = self.builder.get_object("txt_password_confirm")
        file_chooser = self.builder.get_object("filechooser_key")

        # Check for the name
        if len(name.get_text()) == 0:
            MessageBox("Name can't be empty!")
            return False

        # Check for the host
        if len(host.get_text()) == 0:
            MessageBox("Host can't be empty!")
            return False

        # Check for the port
        port_number = port.get_text()
        if len(port_number) == 0:
            MessageBox("Port can't be empty!")
            return False
        elif not port_number.isdigit() or int(port_number) <= 0 or int(port_number) > 65565:
            MessageBox("Port must be between 1 and 65565")
            return False

        # Check for the user
        if len(user.get_text()) == 0:
            MessageBox("User can't be empty!")
            return False

        # If switch key is On, the filechooser must have a file
        if switch_key.get_active():
            # If file chooser haven't any file, return error
            if file_chooser.get_filename() is None:
                MessageBox("You must select a key file")
                return False
        else:
            # Check if password is empty
            if len(password.get_text()) == 0:
                MessageBox("Password can't be empty!")
                return False

            # Check if the password are the same, if not, return error
            if password.get_text() != confirm_password.get_text():
                MessageBox("The passwords not match")
                return False

        # If all pass, return True
        return True

    def save_connection(self):
        # Get all object that need be validated
        name = self.builder.get_object("txt_name")
        host = self.builder.get_object("txt_host")
        port = self.builder.get_object("txt_port")
        user = self.builder.get_object("txt_user")
        switch_key = self.builder.get_object("switch_use_key")
        password = self.builder.get_object("txt_password")
        file_chooser = self.builder.get_object("filechooser_key")

        # Create a new Connection
        if self.connection is None:
            self.connection = Connection()

        self.connection.name = name.get_text()
        self.connection.host = host.get_text()
        self.connection.port = port.get_text()
        self.connection.user = user.get_text()
        self.connection.use_key = switch_key.get_active()
        self.connection.key_path = file_chooser.get_filename()
        self.connection.password = password.get_text()

        # Save the connection
        saved = self.connection.save()

        # Delete the Tunnels
        self.connection.delete_tunnels()

        # Now saved the tunnels
        for tunnel in self.tunnels.get_tunnels():
            # Set the ID connection
            tunnel.id_connection = self.connection.id

            # Save the Tunnel
            tunnel.save()

        # return if is saved or not
        return saved
