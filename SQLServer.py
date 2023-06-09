import pyodbc

class SQLServer:
    def __init__(self, server, database):
        self.server = server
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = pyodbc.connect(f"DRIVER={{SQL Server}};SERVER={self.server};DATABASE={self.database};Trusted_Connection=yes")
            self.cursor = self.connection.cursor()
            print("Connection established successfully!")
        except Exception as e:
            print(f"Error connecting to SQL Server: {e}")

    def disconnect(self):
        try:
            self.connection.close()
            print("Connection closed successfully!")
        except Exception as e:
            print(f"Error disconnecting from SQL Server: {e}")

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return rows
        except Exception as e:
            print(f"Error executing query: {e}")

    def query_table(self, table):
        try:
            self.cursor.execute(f"SELECT * FROM {table}")
            rows = self.cursor.fetchall()
            return rows
        except Exception as e:
            print(f"Error executing query: {e}")