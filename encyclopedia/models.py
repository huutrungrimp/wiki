from django.db import models
from django.core.exceptions import ValidationError

class MyEntries(models.Model):
    title = models.CharField(max_length = 20, unique=True)
    content = models.TextField()
    
    class Meta:
        verbose_name_plural = "My Entries"
    def __str__(self):
        return self.title