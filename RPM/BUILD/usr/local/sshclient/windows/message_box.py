# -*- coding: utf-8 -*-
import settings
from gi.repository import Gtk


class MessageBox:
    glade_file = settings.APP_PATH + "/ui/message_box.glade"
    main_object = None
    handler_class = None
    builder = None
    window = None
    text = None

    def __init__(self, text):
        # Set some properties
        gtk_settings = Gtk.Settings.get_default()
        gtk_settings.props.gtk_button_images = True
        self.text = text

        # Build the Window
        self.build_window()

        # Connect the signals
        self.connect_events()

    def build_window(self):
        # Get the builder
        self.builder = Gtk.Builder()

        # inflate the layout
        self.builder.add_from_file(self.glade_file)

        self.window = self.builder.get_object("message_box")
        self.window.set_markup(self.text)

        self.window.show_all()
        self.window.run()
        self.window.destroy()

    def connect_events(self):
        # Connect the signals
        self.handler_class = None
        self.builder.connect_signals(self.handler_class)
