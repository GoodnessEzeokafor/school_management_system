from django.contrib import admin
from .models import StudentProfile
# Register your models here.


@admin.register(StudentProfile)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('students_name', 'student_class')
    list_filter = ('student_class',)
    order_by = ('-student_class',)


    def students_name(self, obj):
        return '{} {} {}'.format(obj.first_name, obj.other_name, obj.last_name).title()





