from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

TEACHER_CLASS = (
    ('jss1', 'JSS1'),
    ('jss2', 'JSS2'),
    ('jss3', 'JSS3'),
    ('ss1', 'SS1'),
    ('ss2', 'SS2'),
    ('ss3', 'SS3')
)
GENDER = (
    ('male', "Male"),
    ('female', "Female"),
    ('other', 'Rather Not Mention')
)


class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=300, blank=False, null=False)
    other_name = models.CharField(max_length=300, blank=False, null=False)
    last_name = models.CharField(max_length=300, blank=False, null=False)
    mugshot = models.ImageField(upload_to='teachers/images/%Y/%m/%d')
    gender = models.CharField(max_length=50,choices=GENDER, default='male')
    teacher_class = models.CharField(max_length=50, choices=TEACHER_CLASS, default='jss1')
    qualification = models.FileField(upload_to='teacher/file/%Y/%m/%d')
    date_of_birth = models.DateField(auto_now_add=False)
    date_admitted = models.DateField(auto_now_add=False)
    date_created  = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    address = models.TextField(blank=True)


    class Meta:
        verbose_name = "Teacher's Profile"
    
    def __str__(self):
        return "{} {} {}".format(self.first_name, self.other_name, self.last_name)


    def get_absolute_url(self):
        return reverse("teacher_profile:teacher_profile_detail", args = [self.pk])


