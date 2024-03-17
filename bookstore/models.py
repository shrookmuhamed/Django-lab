from django.db import models
from author.models import author
from django.shortcuts import  reverse, get_object_or_404

# Create your models here.

class book(models.Model):
    name = models.CharField(max_length=100)
    # image = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='bookstore/images/', null=True)
    price = models.IntegerField(default=10, null=True)
    pages = models.IntegerField(default=10, null=True) 
    created_at = models.DateTimeField(auto_now_add=True, null=True) # create
    updated_at = models.DateTimeField(auto_now=True, null=True)  # update
    author = models.ForeignKey(author, on_delete=models.CASCADE,
                              null=True, related_name='books') 

    def __str__(self):
        return f"{self.name}"


    @property
    def image_url(self):
        return f'/media/{self.image}'
    

    @property
    def show_url(self):
        url = reverse('bookstore.show', args=[self.id])
        return url

