from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Info(models.Model):
    location= models.CharField(max_length= 50)
    street= models.CharField(max_length= 50)
    phone_number = PhoneNumberField()
    email= models.EmailField(max_length=30, null=True, blank=True)
    
    def __str__(self):
        return 'Business Info'