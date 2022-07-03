from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView

from .forms import LoginUserForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'accounts/login.html'
    extra_context = {'title': 'Login page'}


def logout_page(request):
    logout(request)
    return redirect('/accounts/login_page')
