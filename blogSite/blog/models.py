
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100,blank=False)
    content = models.TextField(max_length=3000, blank=False)
    slug = models.CharField(max_length=50, blank=False)
    created_at =models.DateTimeField(auto_created=True,auto_now_add=True,auto_now=False)
    updated_at = models.DateTimeField(auto_created=True,auto_now_add=True)
