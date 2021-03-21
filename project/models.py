from django.db import models
from django.urls import reverse

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=40)
    #Drop down menu pip install django-filter
    TYPE = (
        ('office','office'),
        ('Redisential', 'Redisential'),
        ('Commercial', 'Commercial')
    )
    type = models.CharField(max_length = 50, null=True, choices=TYPE)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image')


    def __str__(self):
        return self.title
    
# function for project detail page
    def get_absolute_url(self):
        return reverse('project:project_detail', kwargs={
            'project_id': self.id
            })
        

