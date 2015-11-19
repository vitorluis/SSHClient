# -*- coding: utf-8 -*-
from pprint import pprint


class MainWindowEvents:

    window = None
    builder = None

    def __init__(self, window, builder):
        # Copy the parameters
        self.window = window
        self.builder = builder

    def on_connections_tree_cursor_changed(self, tree):
        (model, treeiter) = tree.get_selection().get_selected_rows()
        pprint(model[treeiter][1])
