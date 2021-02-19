# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Geocafe(models.Model):
    post_code = models.CharField(max_length=10)
    addr = models.CharField(max_length=40)
    name = models.CharField(max_length=20)
    x = models.CharField(max_length=50)
    y = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    open = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    def __str__(self):
        return self.name
