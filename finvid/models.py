from django.db import models

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    publish_datetime = models.DateTimeField()
    thumbnail = models.URLField()
    video_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title
    
    class Meta:
        # Sort by publish_datetime in descending order
        ordering = ['-publish_datetime']
