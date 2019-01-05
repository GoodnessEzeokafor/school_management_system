from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateResponseMixin, View
from .forms import ModuleFormset
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
   
)
from django.views.generic.detail import DetailView
from .models import (
    Course,
    Module,
    Content,
    Subject
)

from django.db.models import Count
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from teachers.models import TeacherProfile
from students.forms import CourseEnrollForm


from django.forms.models import modelform_factory
from django.apps import apps

# Create your views here.


# Course
class OwnerMixin(object):
    def get_queryset(self):
        qs = super(OwnerMixin, self).get_queryset()
        user = TeacherProfile.objects.get(user=self.request.user)
        return qs.filter(owner=user)


class OwnerEditMixin(object):
    def form_valid(self, form):
        form.instance.owner = TeacherProfile.objects.get(user=self.request.user)
        return super(OwnerEditMixin, self).form_valid(form)



class OwnerCourseMixin(OwnerMixin):
    model = Course


class OwnerCourseEditMixin(OwnerCourseMixin, OwnerEditMixin):
    template_name = 'course/manage/course/form.html'
    fields = ['title', 'slug','subject','overview']
    success_url = reverse_lazy('courses:manage_course_list')

# List Course According To The Creator Of The Course
class ManageCourseListView(LoginRequiredMixin,OwnerCourseMixin,ListView):
    template_name = 'course/manage/course/list.html'
    login_url = '/'
    


class CourseCreateView(PermissionRequiredMixin,OwnerCourseEditMixin,CreateView):
    permission_required = 'courses.add_course'


class CourseUpdateView(PermissionRequiredMixin,OwnerCourseEditMixin,UpdateView):
    permission_required = 'courses.change_course'


class CourseDeleteView(PermissionRequiredMixin,OwnerCourseMixin, DeleteView):
    success_url = reverse_lazy('courses:manage_course_list')
    template_name = 'course/manage/course/delete.html'
    permission_required = 'courses.delete_course'



#Displaying Course
class CourseListView(TemplateResponseMixin, View):
    model = Course
    template_name = 'course/courses/list.html'


    def get(self, request,subject=None):
        subjects = Subject.objects.annotate(
            total_courses = Count('courses')
        )
        courses = Course.objects.annotate(
            total_modules=Count('modules')
        )

        if subject:
            subject = get_object_or_404(Subject, slug=subject)
            courses = courses.filter(subject=subject)

        return self.render_to_response({
            'subjects':subjects,
            'subject':subject,
            'courses':courses
        })
        

class CourseDetailView(DetailView):
    model = Course
    template_name = 'course/courses/detail.html'

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['enroll_form'] = CourseEnrollForm(initial={'course':self.object})
        return context

# Module

class CourseModuleUpdateView(TemplateResponseMixin, View):
    template_name = 'course/manage/module/formset.html'
    course = None


    def get_formset(self, data=None):
        return ModuleFormset(instance=self.course, data=data)
    
    def dispatch(self, request, pk):
        self.course = get_object_or_404(Course, id=pk, owner= TeacherProfile.objects.get(user=self.request.user))
        return super(CourseModuleUpdateView, self).dispatch(request, pk)
    
    def get(self,request,*args,**kwargs):
        formset = self.get_formset()
        return self.render_to_response({
            'course':self.course,
            'formset':formset
        })
    
    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('courses:manage_course_list')
        return self.render_to_response({
            'course':self.course,
            'formset':formset
        })



# Content


class ContentCreateUpdateView(TemplateResponseMixin, View):
    module = None
    model = None
    obj = None
    template_name = 'course/manage/content/form.html'

    def get_model(self, model_name):
        if model_name in ['text', 'video', 'file', 'image']:
            return apps.get_model(app_label='courses', model_name=model_name)
        return None
    
    def get_form(self, model, *args, **kwargs):
        Form = modelform_factory(model,exclude =[
            'owner',
            'order',
            'date_created',
            'date_updated'
        ])
        return Form(*args, **kwargs)
    
    def dispatch(self,request, module_id, model_name, id=None):
        self.module = get_object_or_404(Module, id=module_id, course__owner=TeacherProfile.objects.get(user=request.user))
        self.model = self.get_model(model_name)
        if id:
            self.obj = get_object_or_404(self.model, id=id, owner=TeacherProfile.objects.get(user=request.user))
        return super(ContentCreateUpdateView,self).dispatch(request, module_id, model_name, id)
    
    def get(self, request, module_id, model_name, id=None):
        form = self.get_form(self.model, instance=self.obj)
        return self.render_to_response({
            'form':form,
            'object':self.obj
        })
    

    def post(self, request, module_id,model_name, id=None):
        form = self.get_form(self.model, instance=self.obj, data=request.POST, files=request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = TeacherProfile.objects.get(user=request.user)
            obj.save()
            if not id:
                Content.objects.create(module=self.module, item=obj)
            return redirect('courses:module_content_list', self.module.id)
        
        return self.render_to_response({
            'form':form,
            'object':object
        })

class ContentDeleteView(View):
    
    def post(self, request, id):
        content = get_object_or_404(Content, id=id,module__course__owner=TeacherProfile.objects.get(user=self.request.user))
        module = content.module
        content.item.delete()
        content.delete()
        return redirect('courses:module_content_list', module.id)
    


class ModuleContentListView(TemplateResponseMixin, View):
    template_name = 'course/manage/module/content_list.html'


    def get(self,request,module_id):
        module = get_object_or_404(Module,id=module_id,course__owner=TeacherProfile.objects.get(user=self.request.user))
        return self.render_to_response({
            'module':module
        })