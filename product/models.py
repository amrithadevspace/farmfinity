from django.db import models
from farmer.models import Farmer


# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    # farmer_id = models.IntegerField()
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    date = models.DateField()
    product_name = models.CharField(max_length=45)
    photo = models.CharField(max_length=200)
    category = models.CharField(max_length=45)
    description = models.CharField(max_length=200)
    price = models.CharField(max_length=45)
    quantity = models.CharField(max_length=45)
    unit = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'product'


from user.models import User

class Wishlist(models.Model):
    wishlist_id = models.AutoField(primary_key=True)
    # product_id = models.IntegerField(blank=True, null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    # user_id = models.IntegerField(blank=True, null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'wishlist'



