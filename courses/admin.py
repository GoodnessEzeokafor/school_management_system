from django.contrib import admin
from .models import (
    Course, 
    Subject,
    Module,
    Content
)
# Register your models here.



@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('date_created',)
    prepopulated_fields = {'slug': ('title',)}

class ModuleInline(admin.StackedInline):
    model = Module
    

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'subject', 'date_created')
    list_filter = ('date_created','subject', 'owner')
    inlines = [ModuleInline]
    

admin.site.register(Content)