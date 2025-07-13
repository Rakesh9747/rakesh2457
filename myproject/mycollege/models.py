from django.db import models

class CanteenItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='canteen_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class MessItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='mess_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class BakeryItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='bakery_images/', blank=True, null=True)

    def __str__(self):
        return self.name
