# -*- coding: utf-8 -*-
from pprint import pprint

from gi.repository import Gtk
from gi.repository import GLib
from gi.repository import Vte


class Shell:

    terminal = None
    command = None
    window = None
    title = None
    executed = False
    pid = None

    def __init__(self, command, window_title):
        # Command to Run and Env
        self.command = str(command).split(' ')
        print(self.command)
        self.title = window_title

        # Create the terminal
        self.terminal = Vte.Terminal()
        self.terminal.connect("child-exited", self.child_quit)

        # Try to execute
        try:
            self.executed, self.pid = self.terminal.fork_command_full(
                Vte.PtyFlags.DEFAULT,
                None, self.command, [],
                GLib.SpawnFlags.DO_NOT_REAP_CHILD, None, None, None
            )
        except AttributeError:
            self.executed, self.pid = self.terminal.spawn_sync(
                Vte.PtyFlags.DEFAULT,
                None, self.command, [],
                GLib.SpawnFlags.DO_NOT_REAP_CHILD, None, None, None
            )

    def run(self):
        # create a window and add the VTE
        self.window = Gtk.Window()
        self.window.add(self.terminal)
        self.window.connect('delete-event', self.quit_window)

        # Set the Title
        self.window.set_title(self.title)

        # you need to show the VTE
        self.window.show_all()

    def child_quit(self, *args):
        terminal = args[0]
        pprint(terminal.get_child_exit_status())
        self.window.destroy()

    def quit_window(self, *args, **kwargs):
        self.window.destroy()
