from django.db import models

# Create your models here.

JOB_TYPE = (
    ("Full Time", "Full Time"),
    ("Part Time", "Part Time")
)
class Job(models.Model):
    name = models.CharField(max_length= 100)
    # location
    job_description = models.TextField(max_length= 1000)
    published_on = models.DateTimeField(auto_now= True)
    vacancy = models.CharField(max_length= 15, choices= JOB_TYPE)
    salary = models.IntegerField(default= 0)
    category = models.ForeignKey('Category', on_delete= models.CASCADE)
    experience = models.IntegerField(default= 1)
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length= 25)
    
    def __str__(self):
        return self.name