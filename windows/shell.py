# -*- coding: utf-8 -*-
from gi.repository import Gtk
from gi.repository import GLib
from gi.repository import Vte


class Shell:

    terminal = None
    command = None
    window = None
    title = None

    def __init__(self, command, window_title):
        # Command to Run and Env
        self.command = str(command).split(' ')
        print(self.command)
        self.title = window_title

        # Create the terminal
        self.terminal = Vte.Terminal()
        # self.terminal.connect("child-exited", self.quit)

        # spawn_sync() will run a command, in this case it shows a prompt
        try:
            self.terminal.fork_command_full(
                Vte.PtyFlags.DEFAULT,
                None, self.command, [],
                GLib.SpawnFlags.DO_NOT_REAP_CHILD, None, None, None
            )
        except AttributeError:
            self.terminal.spawn_sync(
                Vte.PtyFlags.DEFAULT,
                None, self.command, [],
                GLib.SpawnFlags.DEFAULT, None, None, None
            )

    def run(self):
        # create a window and add the VTE
        self.window = Gtk.Window()
        self.window.add(self.terminal)
        self.window.connect('delete-event', self.quit)

        # Set the Title
        self.window.set_title(self.title)

        # you need to show the VTE
        self.window.show_all()

    def quit(self, *args, **kwargs):
        self.window.destroy()
