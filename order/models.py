from django.db import models
from plants.models import Plants
from user.models import User
from nursery.models import Nursery
from django.utils import timezone

class Order(models.Model):
    orderId     =   models.AutoField(primary_key=True)
    customer    =   models.ForeignKey(User,  on_delete=models.CASCADE)
    plant       =   models.ForeignKey(Plants, on_delete=models.CASCADE)
    seller      =   models.ForeignKey(Nursery, on_delete=models.CASCADE)
    totalPrice  =   models.PositiveIntegerField()
    quantity    =   models.PositiveIntegerField()
    createdAt   =   models.DateTimeField(default=timezone.now())
    address     =   models.CharField(max_length=100)
    pincode     =   models.CharField(max_length=6)
    status      =   models.CharField(max_length=50)

    class Meta:
        db_table    =   'Order'