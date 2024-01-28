from django.contrib import admin

from .models import Post, Category, AboutUs, ContactUs

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(AboutUs)
admin.site.register(ContactUs)