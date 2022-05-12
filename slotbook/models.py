from django.db import models

# Create your models here.
class slot(models.Model):
    Name = models.CharField(max_length=255)
    email = models.EmailField()
    number = models.CharField(max_length=12)
    vaccinecenter = models.CharField(max_length=255)
    pin = models.CharField(max_length=10)
    idnumber = models.CharField(max_length=20)
    appointment = models.CharField(max_length=10)
    dose = models.CharField(max_length=10)
    date = models.DateField(max_length=255)
    time = models.CharField(max_length=255)
