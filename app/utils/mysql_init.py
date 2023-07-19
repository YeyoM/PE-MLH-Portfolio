import os 
import datetime
from peewee import *
from dotenv import load_dotenv

# Load environment variables --> Done for testing purposes
load_dotenv()

# Initialize database as None
mydb = None

# Function to get database connection depending on the environment (Testing or not)
def get_database():
    global mydb

    if mydb is None:
        if os.getenv("TESTING") == "true":
            print("Running in test mode")
            mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
        else:
            mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
                user=os.getenv("MYSQL_USER"),
                password=os.getenv("MYSQL_PASSWORD"),
                host=os.getenv("MYSQL_HOST"),
                port=3306
            )
    
    return mydb

# Function to initialize database to prevent when testing
def db_int():
    # Get database connection
    db = get_database()
    
    if os.getenv("TESTING") == "true":
            db.init('file:memory?mode=memory&cache=shared')
    else:
        db.init(os.getenv("MYSQL_DATABASE"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            host=os.getenv("MYSQL_HOST"),
            port=3306
        )
    

# Models used to create tables
class TimeLinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default = datetime.datetime.now)

    class Meta:
        database = get_database()

class Projects(Model):
    title = CharField()
    image = CharField()
    description = TextField()
    link = CharField()
    created_at = DateTimeField(default = datetime.datetime.now)

    class Meta:
        database = get_database()


def connect():
    # Get the correct database connection
    db = get_database()
    
    try:
        # Initialize database
        db_int()
        # Connect to the database given the previous variable
        db.connect()
        print("Connected to MySQL")
    except OperationalError as e:
        print("Error connecting to MySQL DB")
        print(e)

def create_tables():
    db = get_database()

    try:
        db.create_tables([TimeLinePost])
        db.create_tables([Projects])
        print("Created tables successfully")
    except OperationalError as e:
        print("Error creating tables")
        print(e)