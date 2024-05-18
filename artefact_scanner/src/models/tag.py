from peewee import TextField, DateTimeField, Model, BooleanField
import datetime
from . import db

class Tag(Model): 
    # primary key 
   id = TextField(primary_key=True)
   
   # tag name
   name = TextField(null=False)

    # system generated tags
   system_generated = BooleanField(default=False)
   
   # submitted and updated timestamps
   created_at = DateTimeField(null=False, default=datetime.datetime.now) 

   class Meta:
      database=db
      db_table='tag'
