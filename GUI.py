import tkinter as tk
import SQLServer as db

class GUI:
    def __init__(self, master, server, database):
        self.master = master
        master.title("My Database GUI")

        self.database = db.SQLServer(server, database)
        self.database.connect()

        self.label = tk.Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = tk.Button(master, text="Exe", command=self.query)
        self.greet_button.pack()

        self.close_button = tk.Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def __del__(self):
        self.database.disconnect()

    def query(self):
        print(self.database.query_table("person"))