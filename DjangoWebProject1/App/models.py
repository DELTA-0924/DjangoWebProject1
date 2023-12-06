from django.db import models

# Create your models here.


class Apartaments(models.Model):
    id=models.AutoField(primary_key=True)
    apartament=models.IntegerField()
    floor=models.IntegerField()
    Title=models.CharField(max_length=255)
    kv=models.IntegerField()
    date=models.CharField(max_length=255,blank=True,null=True)
    status=models.CharField(max_length=255)
    price=models.IntegerField()
    busyUntil=models.CharField(max_length=255,blank=True,null=True)
    client=models.CharField(max_length=255,blank=True,null=True)

class Managers(models.Model):
    id=models.AutoField(primary_key=True)
    fullname=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    dataCreated=models.CharField(max_length=255,blank=True,null=True)
    password=models.CharField(max_length=255)
    countDeal=models.IntegerField()
    