from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class UData(models.Model):
    userr=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=254)
    gender=models.CharField(max_length=255)
    mobile=models.CharField(max_length=10)
    city=models.CharField(max_length=255)
    address=models.CharField(max_length=255)





    def __str__(self):
        return self.userr.username

    
