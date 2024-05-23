from django.db import models


class Videos(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    uploaded_at = models.DateTimeField()

    def __str__(self):
        return self.title
