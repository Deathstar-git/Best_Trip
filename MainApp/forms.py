from django.core.files.uploadedfile import UploadedFile
from django.forms import CharField, TextInput, PasswordInput, EmailInput, ImageField, ModelForm,  FileInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


from MainApp.models import Post


class RegisterUserForm(UserCreationForm):
    username = CharField(label='Логин:',
                         widget=TextInput(attrs={'class': 'form-input', 'placeholder': 'Придумайте логин'}))
    email = CharField(label='Почта:',
                      widget=EmailInput(attrs={'class': 'form-input', 'placeholder': 'Ваш e-mail'}))
    password1 = CharField(label='Пароль:',
                          widget=PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Придумайте пароль'}))
    password2 = CharField(label='Повтор пароля:',
                          widget=PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Повторите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = CharField(label='Логин:',
                         widget=TextInput(attrs={'class': 'form-input', 'placeholder': 'Придумайте логин'}))
    password = CharField(label='Пароль:',
                         widget=PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Придумайте пароль'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class AddPostForm(ModelForm):
    title = CharField(label='Название:',
                      widget=TextInput(attrs={'class': 'form-input', 'placeholder': 'Придумайте название'}))
    text = CharField(label='Описание:',
                     widget=TextInput(attrs={'class': 'form-input', 'placeholder': 'Опишите ваш пост'}))
    image_errors = {
        'invalid': "Пожалуйста,выберите корректный файл с изображением",
        'required': "Пожалуйста,выберите файл изображения"
    }
    gallery = ImageField(label='Выберите фото для загрузки:',
                         widget=FileInput(attrs={'multiple': 'multiple', 'accept': "image/*"}),
                         error_messages=image_errors)

    class Meta:
        model = Post
        fields = ('title', 'text', 'gallery')
