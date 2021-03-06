# -*- coding: utf-8 -*-
import settings
from gi.repository import Gtk
from events.new_tunnel_window_events import NewTunnelWindowEvents


class NewTunnelWindow:
    glade_file = settings.APP_PATH + "/ui/new_tunnel_window.glade"
    main_object = None
    handler_class = None
    builder = None
    window = None
    add_tunnel_callback = None

    def __init__(self, add_tunnel_callback):
        # Set some properties
        gtk_settings = Gtk.Settings.get_default()
        gtk_settings.props.gtk_button_images = True
        self.add_tunnel_callback = add_tunnel_callback

        # Build the Window
        self.build_window()

        # Connect the signals
        self.connect_events()

    def build_window(self):
        # Get the builder
        self.builder = Gtk.Builder()

        # inflate the layout
        self.builder.add_from_file(self.glade_file)

        self.window = self.builder.get_object("new_tunnel_window")

        self.window.show_all()

    def connect_events(self):
        # Connect the signals
        self.handler_class = NewTunnelWindowEvents(self.window, self.builder, self.add_tunnel_callback)
        self.builder.connect_signals(self.handler_class)
