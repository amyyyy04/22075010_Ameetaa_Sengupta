from django.db import models

# Create your models here.
from django.db import models

class URL(models.Model):
    long_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.short_code} - {self.long_url}"