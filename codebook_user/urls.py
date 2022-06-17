from click import edit
from django.contrib import admin
from django.urls import path, include
from codebook_user import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path("",user_views.index, name="index"),
    path("home/", user_views.index, name="index"),
    path("index/", user_views.index, name="index"),
    path("user_signup/", user_views.user_signup),
    path("user_signin/", user_views.user_signin),
    path("index/user_signup/", user_views.user_signup),
    path("index/user_signin/", user_views.user_signin),
    path("user_profile/", user_views.user_profile, name="user_profile"),
    path("edit/<str:field>/", user_views.edit, name='edit'),
    path("user_profile/signout/", user_views.signout, name="signout"),
    path("signout", user_views.signout, name="signout"),
    path("forget_password_page/", user_views.forget_password_page, name="forget_password_page"),
    path("reset_forgotten_password_page/<str:email>/",
         user_views.reset_forgotten_password_page, name="reset_forgotten_password_page"),
    path("reset_forgotten_password", user_views.reset_forgotten_password,
         name="reset_forgotten_password"),
    path("get_forget_reset_password_link",
         user_views.get_forget_reset_password_link, name="get_forget_reset_password_link"),
    path("change_password_page/",
         user_views.change_password_page, name="change_password_page"),
    path("change_password", user_views.change_password, name="change_password"),
    
    # friends urls 
    path("add_friend/<str:target_username>/",
         user_views.add_friend, name="add_friend"),
    path("friends_page/", user_views.friends_page, name="friends_page"),
    path("make_friend/<str:target_username>/",
         user_views.make_friend, name="make_friend"),
    path("reject_friend_request/<str:target_username>/",
         user_views.reject_friend_request, name="reject_friend_request"),
    path("delete_friend_request/<str:target_username>/",
         user_views.delete_friend_request, name="delete_friend_request"),
    path("un_friend/<str:target_username>/",
         user_views.un_friend, name="un_friend")
    
]
urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token)
]
