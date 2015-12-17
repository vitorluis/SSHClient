# -*- coding: utf-8 -*-
import settings
from gi.repository import Gtk


class AboutWindow:
    glade_file = settings.APP_PATH + "/ui/about_window.glade"
    main_object = None
    handler_class = None
    builder = None
    window = None

    def __init__(self):
        # Set some properties
        gtk_settings = Gtk.Settings.get_default()
        gtk_settings.props.gtk_button_images = True

        # On Unity, unable the system to put the menu bar on the top
        gtk_settings.props.gtk_shell_shows_menubar = False

        # Build the Window
        self.build_window()

    def build_window(self):
        # Get the builder
        self.builder = Gtk.Builder()

        # inflate the layout
        self.builder.add_from_file(self.glade_file)

        self.window = self.builder.get_object("about_window")

        # Show the Window
        self.window.show_all()

        # Destroy the window
        self.window.run()
        self.window.destroy()
