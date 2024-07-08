from django.contrib.auth.views import LoginView
from django.shortcuts import redirect


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'


def root_view(request):
    return redirect('/accounts/login/')
