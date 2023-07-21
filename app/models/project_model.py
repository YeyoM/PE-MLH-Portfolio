from peewee import *
import datetime
from app.utils.get_database import get_database

class Project(Model):
    title = CharField()
    image = CharField()
    description = TextField()
    link = CharField()
    created_at = DateTimeField(default = datetime.datetime.now)

    class Meta:
        database = get_database()