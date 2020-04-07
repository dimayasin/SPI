from __future__ import unicode_literals
from django.db import models
from django.db import connection
import re #, bcrypt
import datetime

PN_REGEX = re.compile(r'^[a-zA-Z0-9.-\/#]+$')

class Part_Manager(models.Manager):
    def validatePartsData(self, postData):
        errors = []
        mytime=datetime.datetime.strptime(postData['date'], '%Y-%m-%d').date()
        time2 = datetime.datetime.today().date()
        if len(postData['pn']) < 1:
            errors.append("Part number should be more than 1 character long")
        if not PN_REGEX.match(postData['pn']):
            errors.append("Part number should contain: Letters, numbers, or one of these characters(. - / \\ or #)")
        if mytime >= time2 :
            errors.append("Birth date shouldn't be a current or future date.")
        return errors
    



class Parts(models.Model):
    pn=models.CharField(max_length=255)
    source=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    part_type=models.CharField(max_length=255)
    fleet=models.CharField(max_length=255)
    ata=models.CharField(max_length=255)
    uom=models.CharField(max_length=255)
    cond=models.CharField(max_length=255)
    date=models.DateField(default= datetime.date.today)
    price=models.FloatField()
    object = Part_Manager()

