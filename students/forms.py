from django import forms
from .models import StudentProfile
from django.contrib.auth import get_user_model 
from courses.models import Course

User = get_user_model()

class StudentCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('email',)


    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise form.ValidationError("Password didn't match")
        return password2



    def save(self, commit=True):
        user = super(StudentCreationForm,self).save(commit=False)
        if commit:
            user.student = True
            user.set_password(self.cleaned_data.get('password1'))
            user.save()
        return user





class StudentProfileCreateForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        exclude = ('date_created', 'date_updated')

    def save(self, commit=True):
        user = super(StudentProfileCreateForm, self).save(commit=False)
        if commit:
            user.student = True
            user.save()
        return user
    
    



class CourseEnrollForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.HiddenInput)
    