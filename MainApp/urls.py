from django.urls import path
# from . import views
from .views import *

urlpatterns = [
    path('',  MainPage.as_view(), name='main'),
    path('login', LoginUser.as_view(), name='login'),
    path('register', RegisterUser.as_view(), name='register'),
    path('my', ProfilePage.as_view(), name='my'),
    path('logout', logout_user, name='logout'),
    path('add_post', AddPostPage.as_view(), name='add_post')
]
