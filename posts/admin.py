from pressroom.posts.models import Post, PostAdmin
from django.contrib import admin

admin.site.register(Post, PostAdmin)