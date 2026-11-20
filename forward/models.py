from django.db import models
from complaint.models import Complaint
# Create your models here.
class Forward(models.Model):
    forward_id = models.AutoField(primary_key=True)
    # complaint_id = models.IntegerField()
    complaint=models.ForeignKey(Complaint,on_delete=models.CASCADE)
    farmer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'forward'
