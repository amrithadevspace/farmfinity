from django.db import models
from order.models import Order
# Create your models here.
class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    # order_id = models.CharField(max_length=45)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    amount = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    payment_method = models.CharField(max_length=45)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'payment'
