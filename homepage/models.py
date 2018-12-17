from django.db import models

class Reservation(models.Model):
    fullname=models.CharField(max_length=50);
    email=models.EmailField(max_length=100)
    date=models.DateField();
    time=models.TimeField();
    party_size=models.IntegerField();
    phone_no=models.CharField(max_length=30);
    def __str__(self):
        return self.fullname;