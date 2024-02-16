from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        app_label = 'delivery_api'

class Item(models.Model):
    TYPE_CHOICES = (
        ('perishable', 'Perishable'),
        ('non_perishable', 'Non-Perishable'),
    )
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    description = models.CharField(max_length=100)

    class Meta:
        app_label = 'delivery_api'

 
class Pricing(models.Model):
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE)
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    zone = models.CharField(max_length=50)
    base_distance_in_km = models.PositiveIntegerField()  # Set default value to 5
    km_price = models.DecimalField(max_digits=5, decimal_places=2)  # Set default value to 1.5
    fix_price = models.DecimalField(max_digits=5, decimal_places=2)  # Set default value to 10

    class Meta:
        app_label = 'delivery_api'


     
