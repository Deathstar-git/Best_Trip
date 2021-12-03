from django.urls import path
# from . import views
from .views import *

urlpatterns = [
    path('',  MainPage.as_view(), name='main'),
    path('login', LoginUser.as_view(), name='login'),
    path('register', RegisterUser.as_view(), name='register'),

]
