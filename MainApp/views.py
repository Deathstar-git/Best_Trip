from django.core.files.base import ContentFile
from django.http import HttpResponseNotFound, HttpResponseRedirect
# from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from .utils import *
from django.views.generic import ListView, CreateView
from .models import *
from django.contrib.auth.views import LoginView
from .forms import RegisterUserForm, LoginUserForm, AddPostForm
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect


class MainPage(DataMixin, ListView):
    model = Post
    template_name = 'MainApp/main_page.html'
    context_object_name = 'posts'

    # def render_to_response(self, context, **response_kwargs):
    #     response = super().render_to_response(context, **response_kwargs)
    #     response.set_cookie('pl_id', 1)
    #     return response

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    # def get_queryset(self):
    #     return Song.objects.filter(playlist__pk=1)


class LoginUser(DataMixin,  LoginView):
    form_class = LoginUserForm  # форма авторизации from .forms import LoginUserForm
    template_name = 'MainApp/login.html'  # htmlка для отображения

    def get_context_data(self, *, object_list=None, **kwargs):
        pl_id = 1
        if self.request.method == 'GET':
            if 'pl_id' in self.request.COOKIES:
                pl_id = self.request.COOKIES['pl_id']
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация', pl_id=pl_id)
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse('my')  # на какую страничку перейти в случае успеха


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'MainApp/register.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        u = form.save(commit=False)
        u.save()
        Account.objects.create(user=u)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('login')


class ProfilePage(DataMixin, ListView):
    model = Post
    template_name = 'MainApp/profile_page.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Профиль')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        print(self.request.user.pk)
        try:
            acc = Account.objects.get(user_id=self.request.user.pk)
            return Post.objects.filter(author_id=acc.pk)
        except ObjectDoesNotExist:
            return redirect('main')


class AddPostPage(DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'MainApp/add_post.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавить новый пост')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        p = form.save(commit=False)
        p.author = Account.objects.get(user_id=self.request.user.pk)
        p.save()
        for f in self.request.FILES.getlist('gallery'):
            data = f.read()  # Если файл целиком умещается в памяти
            img = PostGallery.objects.create()
            img.img.save(f.name, ContentFile(data))
            img.save()
            p.gallery.add(img)
            p.save()

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('my')


def logout_user(request):
    logout(request)
    return redirect('main')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Всё фигня,давай по новой</h1>', exception)
