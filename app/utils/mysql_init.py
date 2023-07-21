import os 
from peewee import *
from dotenv import load_dotenv
load_dotenv()  # Load environment variables --> Done for testing purposes

from app.utils.get_database import get_database # Get database creation function 

from app.models.timeline_model import TimeLinePost
from app.models.project_model  import Project


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
        db.create_tables([Project])
        print("Created tables successfully")
    except OperationalError as e:
        print("Error creating tables")
        print(e)