from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
# we will be using ORM models to represent our database in oop way so that the gap between relational database and oop can be solved properly
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    # this is dunder str method which are very useful
    def __str__(self):
        return self.title