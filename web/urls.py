from django.urls import re_path, include
from mainpage import views
from django.contrib import admin


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^page/', views.page),
    re_path(r'^addcom/', views.addcom),
    re_path(r'^', views.page),

]
