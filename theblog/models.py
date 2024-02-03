from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
import django.utils.timezone
from ckeditor.fields import RichTextField


class ContactUs(models.Model):
    body = models.TextField()
    # body = RichTextField(blank = True, null = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateField(auto_now_add = True)

    def __str__(self):
         return str(self.post_date)
    

    def get_absolute_url(self):
        return reverse('our_services')

class AboutUs(models.Model):
    body = models.TextField()
    # body = RichTextField(blank = True, null = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateField(auto_now_add = True)

    def __str__(self):
         return str(self.post_date)
    

    def get_absolute_url(self):
        return reverse('our_services')

class Category(models.Model):
    name = models.CharField(max_length = 255)
    body = models.TextField()
    # body = RichTextField(blank = True, null = True)
    snippet = models.CharField(max_length = 255,default="Click Link Above To Lead Blog Post...")
    # snippet = RichTextField(blank = True, null = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateField(auto_now_add = True)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
         return self.name 
    
    def get_absolute_url(self):
        return reverse('our_services')
    

class Post(models.Model):
    title = models.CharField(max_length = 255)
    title_tag = models.CharField(max_length = 255,default="Star Alliance")
    category = models.CharField(max_length = 255,default="coding")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    advert = models.TextField()
    # body = RichTextField(blank = True, null = True)
    post_date = models.DateField(auto_now_add = True)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    image4 = models.ImageField(null=True, blank=True)
    image5 = models.ImageField(null=True, blank=True)
    image6 = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.title + ' | ' + str(self.author)
    

    def get_absolute_url(self):
        return reverse('home')