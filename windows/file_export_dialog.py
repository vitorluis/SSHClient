# -*- coding: utf-8 -*-
from gi.repository import Gtk
from events.file_export_dialog_events import FileExportDialogEvents


class FileExportDialog:
    glade_file = "ui/file_export_dialog.glade"
    handler_class = None
    builder = None
    window = None
    selected_file_callback = None

    def __init__(self, selected_file_callback):
        # Set some properties
        settings = Gtk.Settings.get_default()
        settings.props.gtk_button_images = True

        # On Unity, unable the system to put the menu bar on the top
        settings.props.gtk_shell_shows_menubar = False

        # Set the callback
        self.selected_file_callback = selected_file_callback

        # Build the Window
        self.build_window()

        # Connect the signals
        self.connect_events()

        # Show the Window
        self.window.run()

    def build_window(self):
        # Get the builder
        self.builder = Gtk.Builder()

        # inflate the layout
        self.builder.add_from_file(self.glade_file)

        self.window = self.builder.get_object("file_export_dialog")

    def connect_events(self):
        # Connect the signals
        self.handler_class = FileExportDialogEvents(self.window, self.builder, self.selected_file_callback)
        self.builder.connect_signals(self.handler_class)
