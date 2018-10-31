from django.urls import reverse_lazy
from django.contrib.auth import login
from django.shortcuts import render
from .forms import (
    StudentCreationForm,
    StudentProfileCreateForm,
    CourseEnrollForm
)
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
     FormView

)
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import StudentProfile

from courses.models import Course
from django.contrib.auth.mixins import LoginRequiredMixin
#Create Student Profile




# Create your views here.


# Students Profile


class StudentCreateProfileView(CreateView):
    form_class = StudentProfileCreateForm
    template_name = 'students/profile/profile_form.html'
    success_url = reverse_lazy('student_profile_list')


class StudentListProfileView(ListView):
    model = StudentProfile
    context_object_name = 'students'
    template_name = 'students/students_list/list.html'



class StudentDetailProfileView(DetailView):
    model = StudentProfile
    context_object_name = 'student_details'
    template_name = 'students/profile/dashboard.html'

class StudentUpdateProfileView(UpdateView):
    template_name = 'students/profile/profile_form.html'
    form_class = StudentProfileCreateForm
    success_url = reverse_lazy('student_profile_detail')


class StudentDeleteProfileView(DeleteView):
    model = StudentProfile
    success_url = reverse_lazy('student_profile_list')
    template_name = 'students/profile/delete.html'
    

class StudentEnrollCourseView(LoginRequiredMixin, FormView):
    course = None
    form_class = CourseEnrollForm


    def form_valid(self, form):
        self.course = form.cleaned_data['course']
        self.course.students.add(self.request.user)
        return super(StudentEnrollCourseView,self).form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('student_course_detail', args=[self.course.id])

# Course Students Are Enrolled in
class StudentCourseList(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'students/course/list.html'

    def get_queryset(self):
        qs = super(StudentCourseList, self).get_queryset()
        return qs.filter(students__in=[self.request.user.studentprofile])



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



# Register Students
class StudentRegisterView(CreateView):
    template_name = 'students/student/registration.html'
    success_url = reverse_lazy('home')
    form_class = StudentCreationForm

    def form_valid(self, form):
        result = super(StudentRegisterView, self).form_valid(form)
        cd = form.cleaned_data
        # user = authenticate(email=cd['email'], password=['password1'])
        user = form.save()
        login(self.request, user)
        return result


