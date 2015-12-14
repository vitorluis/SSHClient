# -*- coding: utf-8 -*-
from windows.file_export_dialog import FileExportDialog


class SettingsWindowEvents:

    # Properties
    window = None
    builder = None

    def __init__(self, window, builder):
        # Copy the parameters
        self.window = window
        self.builder = builder

    def on_btn_save_clicked(self, btn):
        pass

    def on_btn_close_clicked(self, btn):
        self.window.destroy()

    def on_btn_export_clicked(self, btn):
        FileExportDialog(self.on_selected_file_callback)

    def on_selected_file_callback(self):
        pass

    def on_btn_import_clicked(self, btn):
        pass
