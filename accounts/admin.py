from django.contrib.auth import get_user_model
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django.contrib import admin

from .forms import (
    UserAdminChangeForm,
    UserAdminCreationForm
)

# Register your models here.
User = get_user_model()


class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm



    list_display = ('email',) # display
    list_filter = ('admin', 'staff', 'is_active', 'student')
    fieldsets = (
        (None, {'fields':('email', 'password')}),
        ('Permissions', {'fields':('admin', 'staff', 'student', 'is_active', 'groups')})
        # ('Group', {'fields'})
    )


    add_fieldsets = (
        (
           None,{
               'classes':('wide',),
               'fields':('email', 'password1', 'password2', 'staff', 'student')
           } 
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal  = ()

admin.site.register(User, UserAdmin)




