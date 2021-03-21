from django.db import models

# Create your models here.
class Services(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    url = models.URLField(blank=True)


    def __str__(self):
        return self.title

# Model for team members
class TeamMember(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title
    



