from django.db import models
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.EmailField(max_length=225)
    password =  models.CharField(max_length=25)
    address = models.CharField(max_length=225)
    phone = models.CharField(max_length=25)
    cartype = models.CharField(max_length=25)
    regno = models.CharField(max_length=25)
    class Meta:
        db_table = "users"

class Car(models.Model):
    car_type = models.CharField(max_length=25, primary_key=True)
    amount =  models.CharField(max_length=20)
    time = models.TimeField()
    class Meta:
        db_table = "cars"

class Appointment(models.Model):
    service =  models.EmailField(max_length=100)
    name =  models.EmailField(max_length=125)
    regno =  models.CharField(max_length=25)
    address = models.CharField(max_length=225)
    phone = models.CharField(max_length=25)
    cartype = models.CharField(max_length=25)
    date = models.CharField(max_length=25)
    time = models.CharField(max_length=25)
    cartype = models.CharField(max_length=25)
    msg = models.CharField(max_length=225)
    class Meta:
        db_table = "appointment"
      