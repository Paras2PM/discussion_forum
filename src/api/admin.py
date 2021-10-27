from django.contrib import admin
from .models import Post, PostLikes

admin.site.register(Post)
admin.site.register(PostLikes)

