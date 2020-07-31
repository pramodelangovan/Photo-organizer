from django.db import models

# Create your models here.
class Photos(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        db_table = "PHOTOS"

class FileLocations(models.Model):
    id = models.AutoField(primary_key=True)
    path = models.TextField(default='~/')
    active = models.BooleanField(default='True')
    
    class Meta:
        db_table = "FILE_LOCATIONS"