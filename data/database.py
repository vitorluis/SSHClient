# -*- coding: utf-8 -*-
import settings
import sqlite3


class DBConnection:

    file = None
    connection = None
    cursor = None

    def __init__(self):
        # Set the DB File
        self.file = settings.DB_FILE

    def open_connection(self):
        # Open the connection
        self.connection = sqlite3.connect(self.file, detect_types=sqlite3.PARSE_COLNAMES)

        # Get the cursor
        self.cursor = self.connection.cursor()

    def execute_query(self, sql):
        # Execute the query
        self.cursor.execute(sql)

        # Commit the changes
        self.connection.commit()

        # Return the affected Rows
        return self.cursor.rowcount

    def select_query(self, sql):
        # Execute the query
        self.cursor.execute(sql)

        # Commit the changes
        self.connection.commit()

        # Return all rows
        return self.cursor.fetchall()

