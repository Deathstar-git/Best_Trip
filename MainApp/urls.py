from django.urls import path, re_path
from . import views
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('', MainPage.as_view(), name='main'),
    path('login', LoginUser.as_view(), name='login'),
    path('register', RegisterUser.as_view(), name='register'),
    path('my', ProfilePage.as_view(), name='my'),
    path('logout', logout_user, name='logout'),
    path('add_post', AddPostPage.as_view(), name='add_post'),
    path('page_with_all_posts', views.page_with_all_posts, name = 'page_with_all_posts'),
    re_path(r'^post_form/(?P<parameter>\w+)$', views.post_form, name="post_form")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
