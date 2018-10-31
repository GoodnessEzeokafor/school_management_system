from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from teachers.models import TeacherProfile
from students.models import StudentProfile
# Create your views here.





def HomePageView(request):
    # teacher_profile = get_object_or_404(TeacherProfile,id=None)
    # student_profile = get_object_or_404(StudentProfile, id=None)
    # # if request.user.teacherprofile:
    # #     message = "Hello" 
    # if request.user.studentprofile:
    #     message = 'Hello'
    context = {
        # 'message':message,
    }
    template_name = 'home.html'
    return render(request, template_name, context)