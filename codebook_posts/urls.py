from django.contrib import admin
from django.urls import path, include
from codebook_user import urls as codebook_user_urls
import codebook_user
import codebook_home
from codebook_posts import views as posts_views 
from codebook_home import urls as codebook_home_urls

urlpatterns = [
    
    path("post_image/", posts_views.post_image_page, name="post_image_page"),
    path("post_video/", posts_views.post_video_page, name="post_video_page"),
    
    path("create_post/<str:field>/", posts_views.create_post, name="create_post"),
    
    path("open_post/<int:postid>/", posts_views.open_post_page ,name="open_post"),
    path("my_posts/", posts_views.my_post_page, name="my_posts"),
    path("delete_my_post/<str:my_postid>/", posts_views.delete_my_post, name="delete_my_post"),
    path("search/", posts_views.search_user, name="search"),
    path("like_post/<str:target_postid>/", posts_views.like_post,name="like_post"),
    path("post_comment/<str:target_postid>/", posts_views.comment, name="post_comment"),
    path("edit_post_page/<int:target_postid>/", posts_views.edit_post_page, name="edit_post_page"),
    path("edit_post/<str:field>/<int:target_postid>/",posts_views.edit_post, name="edit_post"),
    path("notifications/", posts_views.notification_page, name="notification_page"),
    
]
