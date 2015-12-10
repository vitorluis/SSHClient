# -*- coding: utf-8 -*-
from windows.file_export_dialog import FileExportDialog


class SettingsWindowEvents:

    window = None
    builder = None

    def __init__(self, window, builder):
        # Copy the parameters
        self.window = window
        self.builder = builder

    def on_btn_save_clicked(self, btn):
        # First of all, validate the form
        pass

    def on_btn_close_clicked(self, btn):
        self.window.destroy()

    def on_btn_export_clicked(self, btn):
        FileExportDialog(None)
