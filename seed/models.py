from django.db import models
from krishibhavan.models import Krishibhavan
# Create your models here.
class Seed(models.Model):
    seed_id = models.IntegerField(primary_key=True)
    # krishibhavan_id = models.IntegerField()
    krishibhavan=models.ForeignKey(Krishibhavan,on_delete=models.CASCADE)
    date = models.DateField()
    seed_name = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    crop_name = models.CharField(max_length=45)
    discription = models.CharField(max_length=500)
    price = models.CharField(max_length=45)
    unit = models.CharField(max_length=45)
    pnone_number = models.CharField(max_length=45)
    photo = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'seed'
