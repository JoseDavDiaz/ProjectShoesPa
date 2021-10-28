from django.db import models
from django.db.models.deletion import CASCADE
from .user import User

class Account(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, related_name='account', on_delete=models.CASCADE)
	orders= models.IntegerField("Orders",default=0)
	pendingOrder = models.BooleanField("PedingOrder",default=False)
	isActive = models.BooleanField("isActive", default = True)
