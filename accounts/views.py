from django.shortcuts import render, redirect 
from django.views.generic.edit import (
    CreateView
)
from .forms import UserCreateForm,UserLoginForm


from django.urls import reverse_lazy
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login

)
# from django.urls import redirect

# Create your views here.




class SignUp(CreateView):
    template_name = 'accounts/signup.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('home')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        login(request, user)
        print(request.user.is_authenticated)
        return redirect("/dashboard/")
    template_name = 'accounts/login.html'
    context = {
        'form':form
    }
    return render(request, template_name, context)


# def login(request, **kwargs):
#     if request.user.is_authenticated():
#         return redirect('/cadmin/')
#     else:
#         return auth_views.login(request, **kwargs)