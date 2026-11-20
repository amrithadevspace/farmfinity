from django.db import models

# Create your models here.
class Farmer(models.Model):
    farmer_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=45)
    farmer_name = models.CharField(max_length=45)
    gender = models.CharField(max_length=45)
    house_name = models.CharField(max_length=45)
    place = models.CharField(max_length=45)
    post = models.CharField(max_length=45)
    district = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    photo = models.CharField(max_length=200)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    farming_type = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'farmer'
