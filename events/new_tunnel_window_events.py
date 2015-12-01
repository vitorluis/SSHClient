# -*- coding: utf-8 -*-


class NewTunnelWindowEvents:

    window = None
    builder = None
    connections = None

    def __init__(self, window, builder):
        # Copy the parameters
        self.window = window
        self.builder = builder

    def on_btn_add_activate(self, btn):
        pass

    def on_btn_cancel_clicked(self, btn):
        self.window.destroy()
