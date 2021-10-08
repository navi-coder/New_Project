# Create your models here.
from django.db import models

class vehicle(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.CharField(max_length=50)
    location = models.CharField(max_length=20)
    vehicle_number = models.CharField(max_length=10)
    documents = models.FileField()

    def __str__(self):
        return self.name

class driver(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    adhar_number = models.IntegerField()
    document_adhar = models.FileField(null=True)

    def __str__(self):
        return self.name

class assaign_and_unassaign(models.Model):
    driver = models.ForeignKey('driver', on_delete=models.CASCADE, null=True, blank=True)
    vehicle = models.ForeignKey('vehicle', on_delete=models.CASCADE, null=True, blank=True)
    assigned_time = models.DateTimeField()

class order(models.Model):
    from_starting = models.CharField(max_length=50)
    to_destiny = models.CharField(max_length=50)
    truck_type = models.ForeignKey('vehicle', on_delete=models.CASCADE)
    tons = models.IntegerField()
    date_time =  models.DateTimeField()

    def __str__(self):
        return '%s ordered' %  (self.truck_type)


