from django.db import models

class User(models.Model):
    userId  =   models.AutoField(primary_key=True)
    firstName   =   models.CharField(max_length=50)
    lastName    =   models.CharField(max_length=50)
    email       =   models.EmailField(max_length=200)
    password    =   models.CharField(max_length=200)
    phone       =   models.CharField(max_length=10)
    address     =   models.CharField(max_length=200)
    pincode     =   models.CharField(max_length=6)

    def __str__(self):
        return self.email

    class Meta:
        db_table    =   'User'