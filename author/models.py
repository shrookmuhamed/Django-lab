from django.db import models

# Create your models here.

from django.db import models
from django.shortcuts import reverse, get_object_or_404
# Create your models here.


class author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='author/images/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    @property
    def image_url(self):
        return f'/media/{self.image}'

    @property
    def show_url(self) -> str:
        url = reverse("author.show", args=[self.id])
        return url


