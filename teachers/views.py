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
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login
from django.http import HttpResponseRedirect

from accounts.models import User
from django.contrib import messages
from django.contrib.auth.models import Group

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
            user.groups.add(Group.objects.get(name='Instructors'))
            profile = profile_form.save(commit=False)
            profile.user = user # set the user created to the profile
            if 'mugshot' in request.FILES:
                profile.mugshot = request.FILES['mugshot']
            profile.save()
            return HttpResponseRedirect(reverse('teacher_profile:teacher_profile_list'))
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
    # success_url = reverse_lazy('teacher_profile:teacher_profile_detail')
    template_name = 'teachers/profile/profile_form.html'

    # def get_success_url(self):
    #     return HttpResponseRedirect(reverse('teacher_profile:teacher_profile_detail', args=[self.object.id]))




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






def upload_teachers(request):
    '''
    View for uploading Teachers
    '''
    # quiz = get_object_or_404(Quiz,slug=quiz_slug)
    template_name = 'teachers/profile/upload.html'
    if request.method == 'POST':
        csvfile = request.FILES['teacherprofile']  # gets the input field name
        print(csvfile.name)  # prints the csv file name
        if not csvfile.name.endswith('.csv'):
            print("Invalid!!") # prints invalid at the console
            messages.errors(request, "CSV file format not supported")
            return(HttpResponseRedirect('teacherprofile:fail'))
        file_data = csvfile.read().decode("utf-8")  # reads the csv file
        # print(file_data)
        lines = file_data.split("\n") # split using the delimiter
        data_dict = {} # empty dictionary to store the csv data
        print(len(lines))
        for line in lines:
            print(line)
            fields = line.split(',')
            # print(fields)
            user_dict = {
                'email':fields[0],
                'password':fields[1],
                # 'password2':fields[2],
            }
            teacher_profile_dict = {
                'first_name':fields[2],
                'other_name':fields[3],
                'last_name':fields[4],
                'gender':fields[5],
                'mugshot':fields[6],
                'teacher_class':fields[7],
                'date_of_birth':fields[9],
                'date_admitted':fields[9],
                'address':fields[10]
            }
            # print(len(data_dict))
            if data_dict != '':
                user = User.objects.create_user(
                    email=user_dict['email'],
                    password=user_dict['password']
                )
                user.staff = True
                user.save()  # save the user
                user.groups.add(Group.objects.get(name='Instructors'))
                student_profile = TeacherProfile.objects.create(
                    user = user,
                    first_name = teacher_profile_dict['first_name'],
                    other_name = teacher_profile_dict['other_name'],
                    last_name = teacher_profile_dict['last_name'],
                    mugshot = teacher_profile_dict['mugshot'],
                    gender=teacher_profile_dict['gender'],
                    teacher_class = teacher_profile_dict['teacher_class'],
                    date_of_birth = teacher_profile_dict['date_of_birth'],
                    date_admitted = teacher_profile_dict['date_admitted'],
                    address = teacher_profile_dict['address']
                )
                messages.success(request, "File Successfully Uploaded")
            else:
                messages.errors(request, "File not uploaded")
    context = {}
    return render(request, template_name, context)
