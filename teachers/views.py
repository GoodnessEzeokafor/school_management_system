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
from django.urls import reverse_lazy
from django.contrib.auth import login
# Create your views here.

class TeacherListProfileView(ListView):
    model = TeacherProfile
    context_object_name = 'teachers_list'
    template_name = 'teachers/teachers_list/list.html'


class TeacherCreateProfileView(CreateView):
    form_class = TeacherProfileCreateForm
    success_url = reverse_lazy('teacher_profile:teacher_profile_list')
    template_name = 'teachers/profile/profile_form.html'

class TeacherUpdateProfileView(UpdateView):
    form_class = TeacherProfileCreateForm
    success_url = reverse_lazy('teacher_profile:teacher_profile_detail')
    template_name = 'teachers/profile/profile_form.html'

class TeacherDetailProfileView(DetailView):
    model = TeacherProfile
    template_name = 'teachers/profile/dashboard.html'
    context_object_name = 'teacher_detail'

class TeacerDeleteProfileView(DeleteView):
    model = TeacherProfile
    template_name = 'teachers/profile/profile_delete_form.html'
    
class TeacherRegisterView(CreateView):
    template_name = 'teachers/teacher/registration.html'
    form_class = TeacherRegisterForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        result = super(TeacherRegisterView, self).form_valid(form)
        cd = form.cleaned_data
        user = form.save()
        login(self.request, user)
        return result


