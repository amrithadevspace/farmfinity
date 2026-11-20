from django.db import models
from krishibhavan.models import Krishibhavan
from farmer.models import Farmer

# Create your models here.
class FarmingDetails(models.Model):
    farming_details_id = models.AutoField(primary_key=True)
    # farmer_id = models.IntegerField()
    farmer=models.ForeignKey(Farmer,on_delete=models.CASCADE)
    # krishibhavan_id = models.IntegerField()
    krishibhavan=models.ForeignKey(Krishibhavan,on_delete=models.CASCADE)
    article = models.CharField(max_length=500)
    video = models.CharField(max_length=200)
    crop_name = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    discription = models.CharField(max_length=200)
    type = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'farming_details'
