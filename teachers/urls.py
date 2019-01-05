from django.urls import path
from . import views

app_name = 'teacher_profile'


urlpatterns = [
    # path('register/', views.TeacherRegisterView.as_view(), name='teacher_register'),
    path('', views.TeacherListProfileView.as_view(), name='teacher_profile_list'),
    path('profile/create/', views.register, name='teacher_profile_create'),
    path('profile/upload/', views.upload_teachers, name='teacher_profile_upload'),
    path('<int:pk>/profile/detail/', views.TeacherDetailProfileView.as_view(), name='teacher_profile_detail'),
    path('<int:pk>/edit/', views.TeacherUpdateProfileView.as_view(), name='teacher_profile_edit'),
    path('<int:pk>/profile/delete/', views.TeacerDeleteProfileView.as_view(), name='teacher_profile_delete'),
]
