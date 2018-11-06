from django.shortcuts import render
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.views.generic.detail import  DetailView
from django.views.generic.list import ListView
from .models import TeacherProfile

from .forms import (
    TeacherRegisterForm,
    TeacherProfileCreateForm
)
from accounts.forms import UserCreateForm
from django.urls import reverse_lazy
from django.contrib.auth import login
# Create your views here.

class TeacherListProfileView(ListView):
    model = TeacherProfile
    context_object_name = 'teachers_list'
    ordering = ['-teacher_class']
    template_name = 'teachers/teachers_list/list.html'



def register(request):
    if request.method == 'POST':
        user_form = UserCreateForm(data=request.POST)
        profile_form = TeacherProfileCreateForm(
            data = request.POST,
            files = request.FILES
        )
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.staff = True
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user # set the user created to the profile
            if 'mugshot' in request.FILES:
                profile.mugshot = request.FILES['mugshot']
            profile.save()
    else:
        user_form = UserCreateForm()
        profile_form = TeacherProfileCreateForm()
    return render(request,'teachers/profile/create_form.html', {
        'user_form':user_form,
        'profile_form':profile_form
    })


class TeacherUpdateProfileView(UpdateView):
    model = TeacherProfile
    form_class = TeacherProfileCreateForm
    success_url = reverse_lazy('teacher_profile:teacher_profile_detail')
    template_name = 'teachers/profile/profile_form.html'

    def get_success_url(self):
        return reverse_lazy('teacher_profile:teacher_profile_detail', args=[self.object.id])


class TeacherDetailProfileView(DetailView):
    model = TeacherProfile
    template_name = 'teachers/profile/dashboard.html'
    context_object_name = 'teacher_detail'

class TeacerDeleteProfileView(DeleteView):
    model = TeacherProfile
    template_name = 'teachers/profile/profile_delete_form.html'
    success_url = reverse_lazy('teacher_profile:teacher_profile_list')


# Teacher Register View

class TeacherRegisterView(CreateView):
    template_name = 'teachers/teacher/registration.html'
    form_class = TeacherRegisterForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        result = super(TeacherRegisterView, self).form_valid(form)
        cd = form.cleaned_data
        user = form.save()
        return result


