from django.db import models
from nursery.models import Nursery

class Plants(models.Model):
    plantId =   models.AutoField(primary_key=True)
    name    =   models.CharField(max_length=100)
    price   =   models.PositiveIntegerField()
    image   =   models.ImageField(upload_to='pictures/')
    sellerId    =   models.ForeignKey(Nursery, on_delete=models.CASCADE)
    quantity    =   models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table    =   'Plants'