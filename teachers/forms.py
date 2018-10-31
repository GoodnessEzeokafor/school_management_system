from django import forms
from .models import TeacherProfile
from django.contrib.auth import get_user_model


User = get_user_model()


class TeacherProfileCreateForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        exclude = ('date_created', 'date_updated')

    def save(self, commit=True):
        teacher_profile = super(TeacherProfileCreateForm, self).save(commit=False)
        if commit:
            teacher_profile.save()
        return teacher_profile

        

class TeacherRegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('email',)

    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationForm("Password didn't match")
        return password2
    


    def save(self, commit=True):
        user = super(TeacherRegisterForm, self).save(commit=False)
        if commit:
            user.set_password(self.cleaned_data.get('password2'))
            user.staff = True
            user.save()
        return user
