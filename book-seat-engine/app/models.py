from django.db import models

class App(models.Model):
    time_published = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=50)
    
    def __str__(self):
        return self.text
# Create your models here.

class App_second(models.Model):
    time_published = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=50)
    
    def __str__(self):
        return self.text