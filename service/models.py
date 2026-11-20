from django.db import models
from krishibhavan.models import Krishibhavan
# Create your models here.
class Service(models.Model):
    service_id = models.IntegerField(primary_key=True)
    # krishibhavan_id = models.IntegerField()
    krishibhavan=models.ForeignKey(Krishibhavan,on_delete=models.CASCADE)
    date = models.DateField()
    service_name = models.CharField(max_length=45)
    discription = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'service'

