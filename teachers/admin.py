from django.contrib import admin
from .models import TeacherProfile
# Register your models here.



@admin.register(TeacherProfile)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teachers_name', 'teacher_class')
    list_filter = ('teacher_class',)
    list_editable = ['teacher_class']



    def teachers_name(self, obj):
        return "{} {} {}".format(obj.first_name, obj.other_name, obj.last_name).title()
