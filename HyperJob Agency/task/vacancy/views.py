from django.shortcuts import render
from django.views import View
from django.db import models
from vacancy.models import Vacancy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView



# Create your views here.


class MainPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vacancy/main_page.html')


class Vacancies(View):
    def get(self, request, *args, **kwargs):
        context = {'vacancy_lst': Vacancy.objects.all()}
        return render(request, 'vacancy/vacancies_lst.html', context=context)


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'signUp.html'


class MyLoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    template_name = 'login.html'

