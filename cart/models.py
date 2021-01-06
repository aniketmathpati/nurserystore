from django.db import models
from plants.models import Plants
from user.models import User

class Cart(models.Model):
    id  =   models.AutoField(primary_key=True)
    plant =   models.ForeignKey(Plants, on_delete=models.CASCADE)
    customer    =   models.ForeignKey(User, on_delete=models.CASCADE)
    quantity    =   models.PositiveIntegerField()
    totalPrice  =   models.PositiveIntegerField()

    def __str__(self):
        return "{} plants of {} by {} ".format(self.quantity, self.plant.name, self.customer.firstName)

    class Meta:
        db_table = 'Cart'
        