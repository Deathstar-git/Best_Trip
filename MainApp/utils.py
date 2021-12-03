from django.core.handlers.wsgi import WSGIRequest


menu = [{'title': "Мой профиль", 'url_name': 'my'}]


class DataMixin:
    request: WSGIRequest

    def get_user_context(self, **kwargs):
        context = kwargs
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu[0] = {'title': "Войти", 'url_name': 'login'}
        context['menu'] = user_menu
        return context
