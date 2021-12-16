from django.urls import path, re_path
from . import views
from .views import *

urlpatterns = [
    path('',  MainPage.as_view(), name='main'),
    path('login', LoginUser.as_view(), name='login'),
    path('register', RegisterUser.as_view(), name='register'),
    re_path(r'^post_form/(?P<parameter>\w+)$', views.post_form, name="post_form")
]