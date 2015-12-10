# -*- coding: utf-8 -*-
from pprint import pprint


class FileExportDialogEvents:

    window = None
    builder = None
    selected_file_callback = None

    def __init__(self, window, builder, selected_file_callback):
        # Copy the parameters
        self.window = window
        self.builder = builder
        self.selected_file_callback = selected_file_callback

    def on_btn_save_clicked(self, btn):
        # First of all, validate the form
        pass

    def on_btn_cancel_clicked(self, btn):
        self.window.destroy()

    def on_file_export_dialog_file_activated(self, dialog):
        pprint(dialog)
