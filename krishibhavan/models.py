from django.db import models

# Create your models here.
class Krishibhavan(models.Model):
    krishibhavan_id = models.AutoField(primary_key=True)
    krishibhavan_name = models.CharField(max_length=45)
    officer_name = models.CharField(max_length=45)
    place = models.CharField(max_length=45)
    service_area = models.CharField(max_length=45)
    district = models.CharField(max_length=45)
    pin = models.CharField(max_length=45)
    office_address = models.CharField(max_length=45)
    office_photo = models.CharField(max_length=200)
    user_name = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'krishibhavan'

