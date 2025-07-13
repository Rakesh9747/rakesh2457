# mca/models.py
from django.db import models

class MCACourse(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    credits = models.IntegerField()
    
    def __str__(self):
        return self.name

# Register in mca/admin.py