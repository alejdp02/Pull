from django.db import models

# Create your models here.
class Tabla(models.Model):
        item_name = models.CharField(max_length=1000, blank=True, null=True)
        amount = models.IntegerField(default=0, blank=True, null=True)
        shelf_life = models.IntegerField(default=0, blank=True, null=True)
        pull = models.IntegerField(default=0, blank=True, null=True)
        check_restocking = models.BooleanField(default=False, blank=True, null=True)
        
        def __str__(self):
            return self.item_name