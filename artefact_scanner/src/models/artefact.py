from peewee import TextField, DateTimeField, Model
import datetime
from . import db

class Artefact(Model): 
   
   # primary key 
   id = TextField(primary_key=True)
   
   # artefact s3 key
   s3_key = TextField(null=False)

   # artefact description
   description = TextField(null=False, default= "")
   
   # scan status: pending, scanned, failed
   status = TextField(null=False, default="pending")
   
   # artefact tags
   tags = TextField(null=False, default="[]")
   
   # submitted and updated timestamps
   created_at = DateTimeField(null=False, default=datetime.datetime.now) 

   class Meta:
      database=db
      db_table='artefact'
