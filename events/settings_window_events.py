# -*- coding: utf-8 -*-
import shutil
import settings
from windows.file_export_dialog import FileExportDialog
from model.settings import Settings
from windows.message_box import MessageBox


class SettingsWindowEvents:
    # Properties
    window = None
    builder = None
    refresh_list_callback = None

    def __init__(self, window, builder, refresh_list_callback):
        # Copy the parameters
        self.window = window
        self.builder = builder
        self.refresh_list_callback = refresh_list_callback

    def on_btn_save_clicked(self, btn):
        # Get the properties
        x11_forward = self.builder.get_object("chk_enable_x11")
        request_compression = self.builder.get_object("chk_request_compress")
        force_ipv4 = self.builder.get_object("radio_force_ipv4")
        force_ipv6 = self.builder.get_object("radio_force_ipv6")

        # Set the config on Settings
        app_settings = Settings()
        app_settings.x11_forward = int(x11_forward.get_active())
        app_settings.request_compression = int(request_compression.get_active())
        app_settings.force_ipv4 = int(force_ipv4.get_active())
        app_settings.force_ipv6 = int(force_ipv6.get_active())

        # Now, save
        if app_settings.save():
            self.window.destroy()
        else:
            # Show message box about error
            MessageBox("Error while saving the settings, please try again.")

    def on_btn_close_clicked(self, btn):
        self.window.destroy()

    def on_btn_export_clicked(self, btn):
        FileExportDialog()

    def on_btn_import_clicked(self, btn):
        # Get the FileChooser
        file_chooser = self.builder.get_object("file_import_db")

        # Get the file
        file = file_chooser.get_filename()

        # Check if the file is filled
        if file is not None:
            # Copy the file
            shutil.copy(file, settings.DB_FILE)

            # Call the callback to reload the list
            if self.refresh_list_callback is not None:
                self.refresh_list_callback()

            # Show the message box
            MessageBox("Database imported successfully")

