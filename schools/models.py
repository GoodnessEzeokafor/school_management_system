from django.db import models

# Create your models here.


class SchoolProfile(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=254)
    number_of_students = models.PositiveIntegerField(default=0)
    number_of_staff = models.PositiveIntegerField(default=0)
    address  = models.TextField(blank=True, null=True)
    date_school_was_created = models.DateTimeField(auto_now_add=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name  = "School's Profile"
        ordering =('name',)
    

    def __str__(self):
        return "{} - {}".format(self.name, self.email)



