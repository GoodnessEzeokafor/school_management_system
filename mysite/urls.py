"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from pages.views import HomePageView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls', namespace='students_profile')),
    path('teachers/', include('teachers.urls', namespace='teacher_profile')),
    path('courses/', include('courses.urls', namespace='courses')),
    path('', include('accounts.urls', namespace='account')),
    path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
    path('dashboard/', TemplateView.as_view(template_name='index.html'), name='dashboard'),
    path('accordion/', TemplateView.as_view(template_name='accordion.html'), name='accordion'),
    
    # path('alert/', TemplateView.as_view(template_name='alert.html'), name='alert'),
    # path('badge/', TemplateView.as_view(template_name='badge.html'), name='badge'),
    # path('button_group/', TemplateView.as_view(template_name='button-group.html'), name='button'),
    # path('card/', TemplateView.as_view(template_name='cards.html'), name='button-group'),
    # path('dropdown/', TemplateView.as_view(template_name='dropdown.html'), name='card'),
    # path('list_group/', TemplateView.as_view(template_name='index.html'), name='dropdown'),
    # path('list_group/', TemplateView.as_view(template_name='index.html'), name='list-group'),
    # path('media_group/', TemplateView.as_view(template_name='index.html'), name='media-group'),
    # path('modal/', TemplateView.as_view(template_name='index.html'), name='modal'),
    # path('pagination/', TemplateView.as_view(template_name='index.html'), name='pagination'),
    # path('popovers/', TemplateView.as_view(template_name='index.html'), name='popovers'),
    # path('progressbar/', TemplateView.as_view(template_name='index.html'), name='progressbar'),
    # path('tab/', TemplateView.as_view(template_name='index.html'), name='tab'),
    # path('typography/', TemplateView.as_view(template_name='index.html'), name='typography'),
    # path('grid/', TemplateView.as_view(template_name='index.html'), name='grid'),
    # path('forms/', TemplateView.as_view(template_name='form.html'), name='forms'),
    # path('fontawesome/', TemplateView.as_view(template_name='form.html'), name='fontawesome'),
    # path('theme/', TemplateView.as_view(template_name='theme.html'), name='theme'),
    # path('table_basic/', TemplateView.as_view(template_name='table-basic.html'), name='table-basic'),
    # path('table_layout/', TemplateView.as_view(template_name='table-layout.html'), name='table-layout'),
    # path('datatable/', TemplateView.as_view(template_name='table-layout.html'), name='datatable'),    
    # path('maps/', TemplateView.as_view(template_name='maps.html'), name='maps'),    
    # path('invoice/', TemplateView.as_view(template_name='invoice.html'), name='invoice'),    
    # path('forms/', TemplateView.as_view(template_name='index.html'), name='login_1'),
    # path('forms/', TemplateView.as_view(template_name='index.html'), name='login_2'),
    # path('forms/', TemplateView.as_view(template_name='index.html'), name='login_3'),
    # path('forms/', TemplateView.as_view(template_name='index.html'), name='register_1'),
    # path('forms/', TemplateView.as_view(template_name='index.html'), name='register_2'),
    # path('forms/', TemplateView.as_view(template_name='index.html'), name='register_3'),
    # path('forms/', TemplateView.as_view(template_name='index.html'), name='register_4'),
    # path('forms/', TemplateView.as_view(template_name='index.html'), name='lock_1'),
    # path('forms/', TemplateView.as_view(template_name='index.html'), name='lock_2'),
    # path('forms/', TemplateView.as_view(template_name='index.html'), name='reset_password'),
    # path('forms/', TemplateView.as_view(template_name='index.html'), name='pricing'),
    # path('forms/', TemplateView.as_view(template_name='index.html'), name='error_404'),
    # path('forms/', TemplateView.as_view(template_name='index.html'), name='error_505'),
    
    
    


    #Templates
    path('alert/', TemplateView.as_view(template_name='alert.html'), name='alert'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)