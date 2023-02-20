from django.db import models


class Collections(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=255)
    created = models.DateTimeField('date created')


class Planets(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
