from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.

User  = get_user_model()

STUDENT_CLASS = (
    ('JSS1', 'jss1'),
    ('JSS2', 'jss2'),
    ('JSS3', 'jss3'),
    ('SS1', 'ss1'),
    ('SS2', 'ss2'),
    ('SS3', 'ss3')
)
GENDER = (
    ('male', "Male"),
    ('female', "Female"),
    ('other', 'Rather Not Mention')
)

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='studentprofile')
    first_name = models.CharField(max_length=300, blank=False, null=False)
    other_name = models.CharField(max_length=300, blank=False, null=False)
    last_name  = models.CharField(max_length=300, blank=False, null=False)
    mugshot = models.ImageField(upload_to='student/image/%Y/%m/%d')
    gender = models.CharField(max_length=10,choices=GENDER, default='male')
    student_class = models.CharField(max_length=50, choices=STUDENT_CLASS, default='JSS1')
    date_of_birth = models.DateField(auto_now_add=False)
    date_admitted = models.DateField(auto_now_add=False)
    date_created  = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    address = models.TextField(blank=True)
    
    class Meta:
        verbose_name = "Student's Profile"

    def __str__(self):
        return '{} {} {}'.format(self.first_name, self.other_name, self.last_name)
    

    def get_absolute_url(self):
        return reverse("students_profile:student_profile_detail", args=[self.id])
    
    








