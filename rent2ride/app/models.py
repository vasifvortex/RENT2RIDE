

# Contains the Cycle model representing bikes in the database
from django.db import models

class Cycle(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField()
    image = models.ImageField(upload_to='bike_images/', null=True, blank=True)
    class Meta:
        db_table = 'cycle'
    def __str__(self):
        return self.name

class Contact(models.Model):
    message = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15)
    message = models.TextField(max_length=500)
    class Meta:
        db_table = 'contact'
    def __str__(self) :
        return self.name

#class Order(models.Model) :
 ##  name = models.CharField(max_length=90,default="")
   # email = models.CharField(max_length=50,default="")
    #phone = models.CharField(max_length=20,default="")
 #   address = models.CharField(max_length=500,default="")
 #   city = models.CharField(max_length=50,default="")
 #   cycles = models.CharField(max_length=50,default="")
 #   days_for_rent = models.IntegerField(default=0)
  #  date = models.CharField(max_length=50,default="")
    
   # class Meta:
    #    db_table = 'order'
   # def __str__(self):
    #    return self.name
    
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='static/assets')
    bio = models.TextField(blank=True)
   
    def __str__(self):
        return f'{self.user.username} Profile'
