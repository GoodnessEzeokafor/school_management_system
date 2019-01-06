from django.db import models

from students.models import StudentProfile
from courses.models import Course
# Create your models here.


class Grade(models.Model):
    students = models.ManyToManyField(StudentProfile)
    course = models.ForeignKey(Course,on_delete=models.CASCADE, related_name='course_grade')
    test_score = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name = "Student Test Score",
        help_text = "Student Test Score"
    )
    project_score = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name = "Student Project Score",
        help_text = "Student Project Score"
    )
    assignment_score = models.CharField(
        max_length = 255,
        blank=True,
        null=True,
        verbose_name = "Student Assignment Score"
    )
    pass_mark= models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name = "Pass Mark",

    )
    total_marks = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name ="Grade's Pass Mark",
        help_text = "Grade's Total Mark"
    )
    student_total_score = models.CharField(
        max_length=255, 
        blank=True,
        null=True,
        verbose_name = "Student Total Mark",
        help_text = "Student Total Mark"
    )
    date_score_added= models.DateTimeField(
        auto_now_add=True
    )
    date_score_updated = models.DateTimeField(
        auto_now=True
    )
