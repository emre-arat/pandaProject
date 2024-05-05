from django.db import models

# Create your models here.
class Upload(models.Model):
    name = models.CharField(max_length=100,null=True)
    file = models.ImageField(upload_to="images")
    
    def __str__(self):
        return f"Name:{self.name}"
    