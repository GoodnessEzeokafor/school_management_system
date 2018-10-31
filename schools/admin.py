from django.contrib import admin
from .models import SchoolProfile
# Register your models here.



class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number_of_students', 'number_of_staff')
    list_filter = ('created',)
    search_fields = ('name', 'email')

admin.site.register(SchoolProfile, SchoolAdmin)