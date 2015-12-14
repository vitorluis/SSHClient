# -*- coding: utf-8 -*-
from windows.file_export_dialog import FileExportDialog
from model.settings import Settings
from windows.message_box import MessageBox


class SettingsWindowEvents:
    # Properties
    window = None
    builder = None

    def __init__(self, window, builder):
        # Copy the parameters
        self.window = window
        self.builder = builder

    def on_btn_save_clicked(self, btn):
        # Get the properties
        x11_forward = self.builder.get_object("chk_enable_x11")
        request_compression = self.builder.get_object("chk_request_compress")
        force_ipv4 = self.builder.get_object("radio_force_ipv4")
        force_ipv6 = self.builder.get_object("radio_force_ipv6")

        # Set the config on Settings
        settings = Settings()
        settings.x11_forward = int(x11_forward.get_active())
        settings.request_compression = int(request_compression.get_active())
        settings.force_ipv4 = int(force_ipv4.get_active())
        settings.force_ipv6 = int(force_ipv6.get_active())

        # Now, save
        if settings.save():
            self.window.destroy()
        else:
            # Show message box about error
            MessageBox("Error while saving the settings, please try again.")

    def on_btn_close_clicked(self, btn):
        self.window.destroy()

    def on_btn_export_clicked(self, btn):
        FileExportDialog(self.on_selected_file_callback)

    def on_selected_file_callback(self):
        pass

    def on_btn_import_clicked(self, btn):
        pass
