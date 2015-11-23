# -*- coding: utf-8 -*-
from pprint import pprint


class NewConnectionWindowEvents:

    window = None
    builder = None

    def __init__(self, window, builder):
        # Copy the parameters
        self.window = window
        self.builder = builder

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
        pass

    def on_btn_cancel_clicked(self, btn):
        self.window.destroy()
