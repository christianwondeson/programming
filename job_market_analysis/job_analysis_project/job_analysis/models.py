from django.db import models


# Create your models here.
class jobPosting(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    skills = models.TextField()
    salary = models.CharField(max_length=50)
    posting_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
