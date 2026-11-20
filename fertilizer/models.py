from django.db import models
from krishibhavan.models import Krishibhavan
# Create your models here.
class Fertilizer(models.Model):
    fertilizer_id = models.IntegerField(primary_key=True)
    # krishibhavan_id = models.IntegerField()
    krishibhavan=models.ForeignKey(Krishibhavan,on_delete=models.CASCADE)
    date = models.DateField()
    fertilizer_name = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    discription = models.CharField(max_length=200)
    price = models.CharField(max_length=45)
    unit = models.CharField(max_length=45)
    manufacturing_company = models.CharField(max_length=45)
    image = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'fertilizer'

