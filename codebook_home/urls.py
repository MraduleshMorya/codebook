from click import edit
from django.contrib import admin
from django.urls import path,include
from codebook_user import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views as rest_views
from codebook_home import views as home_views 


urlpatterns = [
    path("codebook_home/", home_views.home , name="codebook_home"),
    path("get_data/<str:username>/", home_views.get_api_invokedata, name="get_data"),
    path("report/", home_views.user_report, name="report"),
    path("report/<str:username>/", home_views.user_report1, name="report1"),

]
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('api-token-auth/', rest_views.obtain_auth_token)
]
