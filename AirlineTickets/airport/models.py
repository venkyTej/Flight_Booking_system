from django.db import models

class Airport(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100, default='Enter city')  # default provided, no null/blank needed

    terminals = models.IntegerField()
    contact = models.CharField(max_length=100, blank=True)  # null=False by default, blank=True allows empty form input

    created_at = models.DateTimeField(auto_now_add=True)  # usually you want auto_now_add for created timestamp
    image = models.ImageField(upload_to='airport_images/', null=True, blank=True)  # image optional

    def __str__(self):
        return self.name
