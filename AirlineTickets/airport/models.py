from django.db import models

class Airport(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    terminals = models.IntegerField()
    image = models.ImageField(upload_to='airport_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return self.name

