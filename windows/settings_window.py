# -*- coding: utf-8 -*-
from gi.repository import Gtk
from events.settings_window_events import SettingsWindowEvents
from model.settings import Settings


class SettingsWindow:
    glade_file = "ui/settings_window.glade"
    main_object = None
    handler_class = None
    builder = None
    window = None
    refresh_list_callback = None

    def __init__(self, refresh_list_callback):
        # Set some properties
        settings = Gtk.Settings.get_default()
        settings.props.gtk_button_images = True

        # On Unity, unable the system to put the menu bar on the top
        settings.props.gtk_shell_shows_menubar = False

        # Set the callback
        self.refresh_list_callback = refresh_list_callback

        # Build the Window
        self.build_window()

        # Connect the signals
        self.connect_events()

    def build_window(self):
        # Get the builder
        self.builder = Gtk.Builder()

        # inflate the layout
        self.builder.add_from_file(self.glade_file)

        self.window = self.builder.get_object("settings_window")

        # Call set properties, to check or unckeck the settings
        self.set_properties()

        # Show the Window
        self.window.show_all()

    def connect_events(self):
        # Connect the signals
        self.handler_class = SettingsWindowEvents(self.window, self.builder, self.refresh_list_callback)
        self.builder.connect_signals(self.handler_class)

    def set_properties(self):
        # Load the settings
        settings = Settings()
        settings.load()

        # Get the checkboxes
        x11_forward = self.builder.get_object("chk_enable_x11")
        request_compression = self.builder.get_object("chk_request_compress")
        force_ipv4 = self.builder.get_object("radio_force_ipv4")
        force_ipv6 = self.builder.get_object("radio_force_ipv6")

        # Set the config
        x11_forward.set_active(bool(settings.x11_forward))
        request_compression.set_active(bool(settings.request_compression))
        force_ipv4.set_active(bool(settings.force_ipv4))
        force_ipv6.set_active(bool(settings.force_ipv6))
