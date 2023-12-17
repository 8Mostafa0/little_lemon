from django.db import models

# Create your models here.
class Menu_i(models.Model):
    Name = models.CharField(max_length=90)
    Price = models.IntegerField()
    Discription = models.TextField()
    Img = models.FileField( upload_to='uploads/')
    
    def __str__(self):
        return self.Name