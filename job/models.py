from django.db import models
from django.utils.text import slugify

# Create your models here.

JOB_TYPE = (
    ("Full Time", "Full Time"),
    ("Part Time", "Part Time")
)
def Image_Upload(instance, imagename):
    imagename, extension= imagename.split(".")
    return "jobs/%s/%s.%s"%(instance.id,instance.id,extension)
class Job(models.Model):
    name = models.CharField(max_length= 100)
    # location
    job_description = models.TextField(max_length= 1000)
    published_on = models.DateTimeField(auto_now= True)
    vacancy = models.CharField(max_length= 15, choices= JOB_TYPE)
    salary = models.IntegerField(default= 0)
    category = models.ForeignKey('Category', on_delete= models.CASCADE)
    image = models.ImageField(upload_to= Image_Upload)
    experience = models.IntegerField(default= 1)
    slug= models.SlugField(blank=True, null=True)
    
    def save(self,*args,**kwargs):
        self.slug= slugify(self.name)
        super(Job,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length= 25)
    
    def __str__(self):
        return self.name
    
class Apply(models.Model):
    job = models.ForeignKey('Job', related_name='job_name', on_delete=models.CASCADE)
    name = models.CharField(max_length= 50)
    email = models.EmailField(blank=False, null=False)
    link = models.URLField(blank=False, null=False)
    cv = models.FileField(upload_to="Apply/")
    cover_letter= models.TextField(max_length= 500)
    created_at= models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return self.name