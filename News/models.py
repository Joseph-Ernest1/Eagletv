from django.db import models

# Create your models here.
class News(models.Model):
    headline = models.CharField(max_length=100)
    content = models.TextField
    categori = models.CharField(max_length=100)
    link = models.URLField(blank=True, null=True)
    video_link = models.URLField(blank=True, null=True)
    image = models.URLField(blank=True, null=True)
    reporter = models.CharField(max_length=100)
    date_posted = models.DateTimeField()
    date_updated = models.DateTimeField()

    def __str__(self):
        return self.headline
    
class Contact(models.Model):
    message = models.TextField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)

    
    def __str__(self):
        return self.message
    


