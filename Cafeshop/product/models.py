from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
    picture = models.ImageField(default='customer/default.png',upload_to='customer/',null=True,blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,default="")
    address = models.TextField()

class Promotion(models.Model):
    name = models.CharField(max_length=255, default="")
    s_date = models.DateField()
    e_date = models.DateField()
    promo_desc = models.TextField()
    discount = models.IntegerField(default=0)
    promo_status = models.BooleanField(default=True)
 

class Order(models.Model):
    
    TYPE_BUY = (
        ('Local_buy', 'Local buy'),
        ('Online_buy', 'Online buy')
    )

    total_price = models.FloatField(default=0)
    order_type = models.CharField(max_length=255, choices=TYPE_BUY)
    date = models.DateTimeField(auto_now=True)
    promo_id = models.ForeignKey(Promotion, on_delete=models.CASCADE, null=True)
    c_id = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)    
    finish_flag = models.BooleanField(default=False)

class Drink_info(models.Model):
    
    DRINK_TYPE = (
        ('Hot', 'Hot'),
        ('Iced', 'Iced'),
        ('Frappe', 'Frappe')
    )
    picture = models.ImageField(default='product/default.png',upload_to='product/',null=True,blank=True)
    d_name = models.CharField(max_length=255)
    how_to_make = models.TextField(default='')
    d_desc = models.CharField(max_length=255, default="")
    cost = models.IntegerField()
    drink_type = models.CharField(max_length=50, choices=DRINK_TYPE)
    useable_status = models.BooleanField(default=True)

class Special(models.Model):

    SPECIAl_TYPE = (
        ('Coffee', 'Coffee'),
        ('Juice', 'Juice')
    )
    
    special_type = models.CharField(max_length=50, choices=SPECIAl_TYPE) 
       
class Order_list(models.Model):
    amount = models.IntegerField()
    unit_price = models.FloatField()
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    d_id = models.ForeignKey(Drink_info, on_delete=models.CASCADE)
    special_id = models.ForeignKey(Special, on_delete=models.CASCADE)  
    


class Fruit(models.Model):
    picture = models.ImageField(default='Fruit/default.png',upload_to='Fruit/',null=True,blank=True)
    fruit_name = models.CharField( max_length=30)
    fruit_desc = models.CharField( max_length=50)
    useable_status = models.BooleanField(default=True)

class Option(models.Model):
    picture = models.ImageField(default='Option/default.png',upload_to='Option/',null=True,blank=True)
    option_name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    price = models.FloatField()
    useable_status = models.BooleanField(default=True)


class Juice(models.Model):
    special_id = models.OneToOneField(Special, primary_key=True, on_delete=models.CASCADE)
    fruits = models.ManyToManyField(Fruit, through='Juice_fruit')
    options = models.ManyToManyField(Option, through='Juice_option')

class Juice_fruit(models.Model):
    juice = models.ForeignKey(Juice, on_delete=models.CASCADE)
    fruit = models.ForeignKey(Fruit, on_delete=models.CASCADE)
    amount = models.IntegerField()


class Coffee_and_other(models.Model):
    
    sweetness = models.CharField(max_length=50, default=None)
    specials = models.OneToOneField(Special, on_delete=models.CASCADE, primary_key=True)
    options = models.ManyToManyField(Option, through='Coffee_and_other_option')

class Coffee_and_other_option(models.Model):
    Coffee_and_other = models.ForeignKey(Coffee_and_other, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    amount = models.IntegerField()
    

class Juice_option(models.Model):
    juice = models.ForeignKey(Juice, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    amount = models.IntegerField()
















