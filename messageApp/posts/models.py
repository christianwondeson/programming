from django.db import models

# Create your models here.
# the page with model the characteristics of our data in actual database and convert it from OOPS programming to tabular form
class Post(models.Model):
    text = models.TextField()
    
    def __str__(self):
        return self.text[:50]