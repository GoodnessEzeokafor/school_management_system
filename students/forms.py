from django import forms
from .models import StudentProfile
from django.contrib.auth import get_user_model 
from courses.models import Course





class StudentProfileCreateForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        exclude = ('date_created', 'date_updated', 'user')

    def save(self, commit=True):
        user = super(StudentProfileCreateForm, self).save(commit=False)
        if commit:
            user.student = True
            user.save()
        return user
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class':'form-control'})
        self.fields['last_name'].widget.attrs.update({'class':'form-control'})
        self.fields['other_name'].widget.attrs.update({'class':'form-control'})
        self.fields['gender'].widget.attrs.update({'class':'form-control'})
        self.fields['student_class'].widget.attrs.update({'class':'form-control'})
        self.fields['date_of_birth'].widget.attrs.update({'class':'form-control'})
        self.fields['date_admitted'].widget.attrs.update({'class':'form-control'})
        self.fields['address'].widget.attrs.update({'class':'form-control'})
class CourseEnrollForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.HiddenInput)


