from django.urls import reverse, reverse_lazy
from django.contrib.auth import login
from django.shortcuts import render
from .forms import (
    StudentProfileCreateForm,
    CourseEnrollForm
)
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
     FormView

)
from accounts.forms import UserCreateForm
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import StudentProfile
from courses.models import Course
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from django.contrib import messages
from accounts.models import User
#Create Student Profile




# Create your views here.


# Students Profile


def register(request):
    if request.method == 'POST':
        user_form = UserCreateForm(data=request.POST)
        profile_form = StudentProfileCreateForm(
            data = request.POST,
            files = request.FILES
        )
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.student = True
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user # set the user created to the profile
            if 'mugshot' in request.FILES:
                profile.mugshot = request.FILES['mugshot']
            profile.save()
            return HttpResponseRedirect(reverse('students_profile:student_profile_list'))
    else:
        user_form = UserCreateForm()
        profile_form = StudentProfileCreateForm()
    return render(request,'students/profile/create_form.html', {
        'user_form':user_form,
        'profile_form':profile_form
    })

class StudentListProfileView(ListView):
    model = StudentProfile
    context_object_name = 'students'
    template_name = 'students/students_list/list.html'
    ordering = ['-student_class']



class StudentDetailProfileView(DetailView):
    model = StudentProfile
    context_object_name = 'student_details'
    template_name = 'students/profile/dashboard.html'


class StudentUpdateProfileView(UpdateView):
    model = StudentProfile
    template_name = 'students/profile/profile_form.html'
    form_class = StudentProfileCreateForm
    
    # def get_success_url(self):
    #     return HttpResponseRedirect(reverse('students_profile:student_profile_detail', args=[self.object.id]))




class StudentDeleteProfileView(DeleteView):
    model = StudentProfile
    success_url = reverse_lazy('students_profile:student_profile_list')
    template_name = 'students/profile/delete.html'





class StudentEnrollCourseView(LoginRequiredMixin, FormView):
    course = None
    form_class = CourseEnrollForm
    template_name = 'course/courses/detail.html'


    def form_valid(self, form):
        self.course = form.cleaned_data['course']
        self.course.students.add(self.request.user)
        # StudentProfile.objects.get(user=self.request.user)
        return super(StudentEnrollCourseView,self).form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('student_course_detail', args=[self.course.id])




# Course Students Are Enrolled in
class StudentCourseList(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'students/course/list.html'

    def get_queryset(self):
        qs = super(StudentCourseList, self).get_queryset()
        return qs.filter(students__in=[StudentProfile.objects.get(user=self.request.user)])
        # self.request.user
        


class StudentCourseDetailView(DetailView):
    model = Course
    template_name = 'students/course/detail.html'


    def get_queryset(self):
        qs = super(StudentCourseDetail, self).get_queryset()
        return qs.filter(students__in=[self.request.user])
    
    def get_context_data(self, **kwargs):
        context = super(StudentCourseDetail, self).get_context_data(**kwargs)
        
        # get course object
        course = self.get_object()
        if 'module_id' in self.kwargs:
            #get current module
            context['module'] = course.modules.get(
                id=self.kwargs['module_id']
            )
        else:
            context['module'] = course.modules.all()[0]
        return context






def upload_student(request):
    '''
    View for uploading Students
    '''
    # quiz = get_object_or_404(Quiz,slug=quiz_slug)
    template_name = 'students/profile/upload.html'
    if request.method == 'POST':
        csvfile = request.FILES['studentprofile']  # gets the input field name
        print(csvfile.name)  # prints the csv file name
        if not csvfile.name.endswith('.csv'):
            print("Invalid!!") # prints invalid at the console
            messages.errors(request, "CSV file format not supported")
            return(HttpResponseRedirect('studentprofile:fail'))
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
            student_profile_dict = {
                'first_name':fields[2],
                'other_name':fields[3],
                'last_name':fields[4],
                'gender':fields[5],
                'mugshot':fields[6],
                'student_class':fields[7],
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
                user.student = True
                user.save()  # save the user
                student_profile = StudentProfile.objects.create(
                    user = user,
                    first_name = student_profile_dict['first_name'],
                    other_name = student_profile_dict['other_name'],
                    last_name = student_profile_dict['last_name'],
                    mugshot = student_profile_dict['mugshot'],
                    gender=student_profile_dict['gender'],
                    student_class = student_profile_dict['student_class'],
                    date_of_birth = student_profile_dict['date_of_birth'],
                    date_admitted = student_profile_dict['date_admitted'],
                    address = student_profile_dict['address']
                )
                messages.success(request, "File Successfully Uploaded")
            else:
                messages.errors(request, "File not uploaded")
    context = {}
    return render(request, template_name, context)
