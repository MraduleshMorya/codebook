from django.contrib import admin
from .models import user,friends2,User_model,liked_posts,post_commnets
# Register your models here.

admin.site.register(friends2)
admin.site.register(User_model)
admin.site.register(post_commnets)
admin.site.register(liked_posts)