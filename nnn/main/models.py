from django.db import models

class MyModel(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()

class uslug(models.Model):
    name = models.CharField(max_length=100000)
    id = models.IntegerField(primary_key=True,)

    def __str__(self):
        return self.title
        
class Gorod(models.Model):
    name = models.CharField(max_length=100000)
    id = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'Gorod'

class Cruise(models.Model):
    id = models.CharField(max_length=100000)
    id_uslug = models.IntegerField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)


    class Meta:
        db_table = 'Cruise'

class Booking(models.Model):
    id= models.CharField(max_length=100)
    date_booking = models.DateTimeField(auto_now_add=True)
    id_cruise = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'Booking'