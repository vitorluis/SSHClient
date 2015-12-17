# -*- coding: utf-8 -*-
import shutil
import settings
from windows.message_box import MessageBox


class FileExportDialogEvents:

    dialog = None
    builder = None
    selected_file_callback = None

    def __init__(self, dialog, builder):
        # Copy the parameters
        self.dialog = dialog
        self.builder = builder

    def on_btn_save_clicked(self, btn):
        # Call the function to export the file
        self.export_file()

    def on_btn_cancel_clicked(self, btn):
        self.dialog.destroy()

    def on_file_export_dialog_file_activated(self, dialog):
        # Call the function to export the file
        self.export_file()

    def export_file(self):
        # Get the file
        file = self.dialog.get_filename()

        # If the file is None, copy the DB to selected file
        if file is not None:
            # Copy the file
            shutil.copy(settings.DB_FILE, file)

            # Close the Dialog
            self.dialog.destroy()

            # Show a message
            MessageBox("Database exported successfully")
