# -*- coding: utf-8 -*-
from windows.message_box import MessageBox
from model.connection import Connection


class NewConnectionWindowEvents:

    window = None
    builder = None
    main_window_callback = None

    def __init__(self, window, builder, main_window_callback):
        # Copy the parameters
        self.window = window
        self.builder = builder
        self.main_window_callback = main_window_callback

    def on_switch_use_key_state_set(self, switch, checked):
        # Get the password fields
        password = self.builder.get_object("txt_password")
        confirm_password = self.builder.get_object("txt_password_confirm")
        file_chooser = self.builder.get_object("filechooser_key")

        if checked:
            # Disable them
            password.set_sensitive(False)
            confirm_password.set_sensitive(False)
            file_chooser.set_sensitive(True)
        else:
            # Enable them
            password.set_sensitive(True)
            confirm_password.set_sensitive(True)
            file_chooser.set_sensitive(False)

    def on_btn_save_clicked(self, btn):
        # First of all, validate the form
        if self.validate_form():
            # If OK, save the connection
            if self.save_connection():
                # Run the callback
                if self.main_window_callback is not None:
                    self.main_window_callback()

                # Close the Window
                self.window.destroy()

    def on_btn_cancel_clicked(self, btn):
        self.window.destroy()

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
        elif int(port_number) <= 0 or int(port_number) > 65565:
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
        connection = Connection()
        connection.name = name.get_text()
        connection.host = host.get_text()
        connection.port = port.get_text()
        connection.user = user.get_text()
        connection.use_key = switch_key.get_active()
        connection.key_path = file_chooser.get_filename()
        connection.password = password.get_text()

        # Save the connection
        return connection.save()
