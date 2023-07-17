import os 
import datetime
from peewee import *

# MYSQL Connection
mydb = MySQLDatabase(
        os.getenv("MYSQL_DATABASE"),
        user = os.getenv("MYSQL_USER"),
        password = os.getenv("MYSQL_PASSWORD"),
        host = os.getenv("MYSQL_HOST"),
        port = 3306
    )

# Models
class TimeLinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default = datetime.datetime.now)

    class Meta:
        database = mydb

class Projects(Model):
    title = CharField()
    image = CharField()
    description = TextField()
    link = CharField()
    created_at = DateTimeField(default = datetime.datetime.now)

    class Meta:
        database = mydb

def connect():
    try:
        mydb.connect()
        print("Connected to MySQL")
    except OperationalError as e:
        print("Error connecting to MySQL DB")
        print(e)

def create_tables():
    try:
        mydb.create_tables([TimeLinePost])
        mydb.create_tables([Projects])
        print("Created tables successfully")
    except OperationalError as e:
        print("Error creating tables")
        print(e)