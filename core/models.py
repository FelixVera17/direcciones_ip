from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True, max_length=1000)
    username = models.CharField(max_length=250)
    name = models.CharField(max_length=250)

class MacAddress(models.Model):
    id = models.AutoField(primary_key=True, max_length=10000) 
    ip_address = models.CharField(max_length=250)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE,max_length=10000)
    

