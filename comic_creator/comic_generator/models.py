from django.db import models

class ComicPanel(models.Model):
    text = models.TextField()
    image_url = models.URLField(null=True, blank=True)
