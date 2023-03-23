import SQLServer as db

# Example usage
sql_server = db.SQLServer(server="localhost\SQLExpress", database="college")
sql_server.connect()
result = sql_server.query_table("person")
print(result)
sql_server.disconnect()