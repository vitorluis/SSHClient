# -*- coding: utf-8 -*-
from windows.main_window import MainWindow
from collection.connections import Connections

conn = Connections()
conn.load_connections()

window = MainWindow()
