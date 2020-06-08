# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class EcoAccounts(models.Model):
    player_id = models.AutoField(primary_key=True)
    player = models.CharField(max_length=255)
    player_uuid = models.CharField(max_length=255)
    money = models.FloatField()
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eco_accounts'


class Eventlog(models.Model):
    uuid = models.CharField(max_length=255, blank=True, null=True)
    oldevent = models.FloatField(blank=True, null=True)
    newevent = models.FloatField(blank=True, null=True)
    eventtime = models.DateTimeField(blank=True, null=True)
    playername = models.CharField(max_length=255, blank=True, null=True)
    servercode = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eventlog'
