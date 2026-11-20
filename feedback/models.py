from django.db import models
from user.models import User
from farmer.models import Farmer

# Create your models here.
class Feedback(models.Model):
    feedback_id = models.IntegerField(primary_key=True)
    # user_id = models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    # farmer_id = models.IntegerField()
    farmer=models.ForeignKey(Farmer,on_delete=models.CASCADE)
    feedback = models.CharField(max_length=45)
    date = models.DateField()
    type = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'feedback'

