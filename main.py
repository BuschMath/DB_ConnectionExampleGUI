import SQLServer as db
import tkinter as tk
import GUI as g

# Example usage
#sql_server = db.SQLServer(server="localhost\SQLExpress", database="college")
#sql_server.connect()
#result = sql_server.query_table("person")
#print(result)
#sql_server.disconnect()

root = tk.Tk()
my_gui = g.GUI(root, server="localhost\SQLExpress", database="college")
root.mainloop()