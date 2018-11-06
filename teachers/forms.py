from django import forms
from .models import TeacherProfile
from django.contrib.auth import get_user_model 


User = get_user_model()

class TeacherProfileCreateForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        exclude = ('date_created', 'date_updated','user' )

    def save(self, commit=True):
        teacher_profile = super(TeacherProfileCreateForm, self).save(commit=False)
        if commit:
            teacher_profile.save()
        return teacher_profile
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['user'].widget.attrs.update({'class':'form-control'})
        self.fields['first_name'].widget.attrs.update({'class':'form-control'})
        self.fields['other_name'].widget.attrs.update({'class':'form-control'})
        self.fields['last_name'].widget.attrs.update({'class':'form-control'})
        self.fields['date_of_birth'].widget.attrs.update({'class':'form-control'})
        self.fields['date_admitted'].widget.attrs.update({'class':'form-control'})
        self.fields['address'].widget.attrs.update({'class':'form-control'})

class TeacherRegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    password1.widget.attrs.update({'class':'form-control'})
    class Meta:
        model = User
        fields = ('email',)

    

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationForm("Password didn't match")
        return password2
    


    # def save(self, commit=True):
    #     user = super(TeacherRegisterForm, self).save(commit=False)
    #     if commit:
    #         user.set_password(self.cleaned_data["password1"])
    #         user.staff = True
    #         user.save()
    #     return user

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # self.fields['user'].widget.attrs.update({'class':'form-control'})
    #     self.fields['email'].widget.attrs.update({'class':'form-control'})
    #     self.fields['password1'].widget.attrs.update({'class':'form-control'})