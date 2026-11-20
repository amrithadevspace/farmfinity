from django.db import models
from user.models import User
from product.models import Product
# Create your models here.
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    # user_id = models.CharField(max_length=45)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    # product_id = models.CharField(max_length=45)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.CharField(max_length=45)
    total_amount = models.IntegerField()
    date = models.CharField(max_length=45)
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'order'
