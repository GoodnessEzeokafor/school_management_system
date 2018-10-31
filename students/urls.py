from django.urls import path
from . import views

app_name = 'students_profile'

urlpatterns = [
    path('register/', views.StudentRegisterView.as_view(), name='student_register'),
    path('',views.StudentListProfileView.as_view(), name='student_profile_list'),
    path('profile/create/', views.StudentCreateProfileView.as_view(), name='student_proile_create'),
    path('<int:pk>/profile/', views.StudentDetailProfileView.as_view(), name='student_profile_detail'),
    path('<int:pk>/update/', views.StudentUpdateProfileView.as_view(), name='student_profile_edit'),
    path('<int:pk>/profile/delete/', views.StudentDeleteProfileView.as_view(), name='student_profile_delete'),
    # Student Course Urls
    path('courses/', views.StudentCourseList.as_view(), name='student_course_list'),
    path('enroll-course/', views.StudentEnrollCourseView.as_view(), name='student_enroll_course'),
    path('courses/<pk>/', views.StudentCourseDetailView.as_view(), name='student_course_detail_view'),
    path('courses/<pk>/<module_id>/', views.StudentCourseDetailView.as_view(), name='student_course_module_detail_view')
]








