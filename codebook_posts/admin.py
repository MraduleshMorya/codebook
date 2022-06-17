from django.contrib import admin
from codebook_posts import models
from .models import posts,notifications
# Register your models here.
# admin.site.register(post_text)
# admin.site.register(post_videos)
# admin.site.register(post_image)
class postsAdmin(admin.ModelAdmin):
    list_display = ("username", "postid")

admin.site.register(posts,postsAdmin)
admin.site.register(notifications)

