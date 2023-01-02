from django.db import models

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    publish_datetime = models.DateTimeField()
    thumbnail = models.URLField()
    video_id = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-publish_datetime']
