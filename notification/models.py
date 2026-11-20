from django.db import models
from krishibhavan.models import Krishibhavan
# Create your models here.
class Notification(models.Model):
    notification_id = models.IntegerField(primary_key=True)
    # krishibhavan_id = models.IntegerField()
    krishibhavan=models.ForeignKey(Krishibhavan,on_delete=models.CASCADE)
    notification = models.CharField(max_length=45)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'notification'

