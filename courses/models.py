from django.db import models
from django.contrib.auth import get_user_model
from teachers.models import TeacherProfile

from .fields import OrderField

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


from students.models import StudentProfile
# Create your models here.


User = get_user_model()


class Subject(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True, blank=True, null=True, help_text='Subject Code')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title 

class Course(models.Model):
    owner = models.ForeignKey(TeacherProfile,on_delete=models.CASCADE, related_name='courses_created')
    title = models.CharField(max_length=300)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='courses')
    slug = models.SlugField(unique=True, blank=True, null=True, help_text='Course Code')
    students = models.ManyToManyField(StudentProfile, related_name='courses_joined', blank=True)
    overview= models.TextField(blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    


    def __str__(self):
        return "{} by {}".format(self.title, self.owner)

class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = OrderField(blank=True, for_fields=['course'])
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return '{}. {}'.format(self.order, self.title)

    class Meta:
        ordering = ['order']

class Content(models.Model):
    module = models.ForeignKey(Module, related_name = 'contents', on_delete=models.CASCADE,limit_choices_to={
        'model__in':(
            'text',
            'video',
            'image',
            'file'
        )
    })
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields=['module'])

    class Meta:
        ordering = ['order']
        
class ItemBase(models.Model):
    owner = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE, related_name = '%(class)s_related')
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True
    
    def __str__(self):
        return self.title

    def render(self):
        return render_to_string('course/content/{}.html'.format(self._meta.model_name), {'item':self})

class Text(ItemBase):
    content = models.TextField()

class File(ItemBase):
    file = models.FileField(upload_to='courses/file/%Y/%m/%d')

class Image(ItemBase):
    file = models.FileField(upload_to='courses/images/%Y/%m/%d')




class Video(ItemBase):
    url = models.URLField()

