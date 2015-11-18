# -*- coding: utf-8 -*-
from gi.repository import Gtk
# from handlers.main_window_handler import MainWindowHandler


class MainWindow:
    glade_file = "ui/main_window.glade"
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

        # Main Loop of GTK
        Gtk.main()

    def build_window(self):
        # Get the builder
        self.builder = Gtk.Builder()

        # inflate the layout
        self.builder.add_from_file(self.glade_file)

        self.window = self.builder.get_object("main_window")
        self.window.connect("delete-event", Gtk.main_quit)

        model = Gtk.ListStore(str)
        model.append(["Cliente 1"])
        model.append(["Cliente 1"])
        model.append(["Cliente 1"])
        model.append(["Cliente 1"])
        model.append(["Cliente 1"])
        model.append(["Cliente 1"])
        model.append(["Cliente 1"])
        model.append(["Cliente 1"])
        model.append(["Cliente 1"])
        model.append(["Cliente 1"])
        lista = self.builder.get_object('connections_tree')

        column = Gtk.TreeViewColumn('Connections', Gtk.CellRendererText(), text=0)
        column.set_clickable(True)
        column.set_resizable(True)
        lista.append_column(column)
        lista.set_model(model)

        model1 = Gtk.ListStore(str, str)
        model1.append(["Property", "Value"])
        model1.append(["Property", "Value"])
        model1.append(["Property", "Value"])
        model1.append(["Property", "Value"])
        model1.append(["Property", "Value"])

        lista = self.builder.get_object('connections_info_tree')
        vbox = self.builder.get_object('vbox_main')

        column = Gtk.TreeViewColumn('Property', Gtk.CellRendererText(), text=0)
        column.set_clickable(False)
        column.set_resizable(True)
        lista.append_column(column)

        column = Gtk.TreeViewColumn('Value', Gtk.CellRendererText(), text=1)
        column.set_clickable(False)
        column.set_resizable(True)
        lista.append_column(column)
        lista.set_model(model1)

        self.window.show_all()

    def connect_events(self):
        # Connect the signals
        self.handler_class = None
        self.builder.connect_signals(self.handler_class)
