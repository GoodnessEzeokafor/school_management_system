from django.shortcuts import render
from django.views.generic.edit import (
    CreateView
)
from .forms import UserCreateForm
from django.urls import reverse_lazy

# Create your views here.


class SignUp(CreateView):
    template_name = 'accounts/signup.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('home')







