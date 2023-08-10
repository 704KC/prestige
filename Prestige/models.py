   
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    role = models.CharField(max_length=255)

class Property(models.Model):
    property_name = models.CharField(max_length=255)
    property_type = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    maps = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    photos = models.ImageField(upload_to='property_images/')
    
class Meta:
    verbose_name = "Property"
    verbose_name_plural = "Properties"

class Rent(models.Model):
    property = models.ForeignKey(Property ,on_delete=models.CASCADE)
    price = models.DecimalField( max_digits=10,decimal_places=2)
    text=models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
class Meta:
    verbose_name_plural = 'rent'
def __str__(self):
    return self.text[:50] + "..."  

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    comment = models.TextField()

class Lease(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    tenant = models.ForeignKey(User, on_delete=models.CASCADE)
    lease_status = models.CharField(max_length=255)
    lease_date = models.DateField()
class Meta:
    verbose_name_plural = 'leases'   
def __str__(self):
    return self.lease_status[:.50]+"..."
     

class Rating(models.Model):
    tenant = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    rating = models.IntegerField()

class Payment(models.Model):
    lease = models.ForeignKey(Lease, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField("payment_date")
class Meta:
    verbose_name_plural='payments'    
    
class Contactus(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField()
    message=models.CharField(max_length=3000)    
class Meta:    
    verbose_name_plural='contactus'    