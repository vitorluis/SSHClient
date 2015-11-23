# -*- coding: utf-8 -*-
from gi.repository import Gtk


class NewConnectionWindow:
    glade_file = "ui/new_connection_window.glade"
    main_object = None
    handler_class = None
    builder = None
    window = None

    def __init__(self):
        # Set some properties
        settings = Gtk.Settings.get_default()
        settings.props.gtk_button_images = True

        # Build the Window
        self.build_window()

        # Connect the signals
        self.connect_events()

    def build_window(self):
        # Get the builder
        self.builder = Gtk.Builder()

        # inflate the layout
        self.builder.add_from_file(self.glade_file)

        self.window = self.builder.get_object("new_connection_window")

        # Set the placeholders
        host = self.builder.get_object("txt_name")
        host.set_placeholder_text("Name")
        self.window.show_all()

    def connect_events(self):
        # Connect the signals
        self.handler_class = None
        self.builder.connect_signals(self.handler_class)