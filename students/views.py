from django.urls import reverse_lazy
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
    
    def get_success_url(self):
        return reverse_lazy('students_profile:student_profile_detail', args=[self.object.id])


class StudentDeleteProfileView(DeleteView):
    model = StudentProfile
    success_url = reverse_lazy('students_profile:student_profile_list')
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
        return qs.filter(students__in=[self.request.user])



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



