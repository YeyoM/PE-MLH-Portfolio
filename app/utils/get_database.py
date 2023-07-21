import os
from peewee import *

# Initialize database as None
mydb = None

# Function to get database connection depending on the environment (Testing or not)
def get_database():
    global mydb

    if mydb is None:
        if os.getenv("TESTING") == "true":
            print("Running in test mode")
            mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri = True)
        else:
            mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
                user = os.getenv("MYSQL_USER"),
                password = os.getenv("MYSQL_PASSWORD"),
                host = os.getenv("MYSQL_HOST"),
                port = 3306
            )
    
    return mydb