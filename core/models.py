from django.db import models
from django.utils import timezone

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=250, unique=True)
    name = models.CharField(max_length=250)

class MacAddress(models.Model):
    ip_address = models.CharField(max_length=250)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mac_addresses')
    date_registered=models.DateTimeField(default=timezone.now())
