from django.db import models
from user.models import User
from farmer.models import Farmer
# Create your models here.
class Complaint(models.Model):
    complaint_id = models.AutoField(primary_key=True)

    # user_id = models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    # farmer_id = models.IntegerField()
    farmer=models.ForeignKey(Farmer,on_delete=models.CASCADE)
    date = models.DateField()
    complaint = models.CharField(max_length=400)
    reply = models.CharField(max_length=200)
    type = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'complaint'


