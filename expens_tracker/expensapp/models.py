from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    phone=models.CharField(max_length=100,unique=True)





class Expense(models.Model):

    payment_choices=(
        (None,"Select"),
        ("card","card"),
        ("upi","upi"),
        ("cash","cash")
    )


    category_choices=(
        (None,"Select"),
        ("Food","Food"),
        ("Travel","Travel"),
        ("Healthcare","Healthcare"),
        ("Miscellaneus","Miscellaneus")

    )


    title=models.CharField(max_length=100)

    category=models.CharField(max_length=100,choices=category_choices,default="Select",null=True,blank=False)

    amount=models.FloatField()

    payment_method=models.CharField(max_length=20,choices=payment_choices,default="Select",null=True,blank=False)

    created_at=models.DateField(auto_now_add=True)

    updated_at=models.DateField(auto_now=True)

    owner=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.title

