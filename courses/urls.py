from django.urls import path, re_path
from . import views

app_name = 'courses'

urlpatterns = [
    path('mine/', views.ManageCourseListView.as_view(), name='manage_course_list'),
    path('create/', views.CourseCreateView.as_view(), name='course_create_view'),
    path('<pk>/edit/', views.CourseUpdateView.as_view(), name='course_edit_view'),
    path('<pk>/delete/', views.CourseDeleteView.as_view(), name='course_delete_view'),
    path('<pk>/module/', views.CourseModuleUpdateView.as_view(), name='course_module_update'),
    path('module/<int:module_id>/content/<model_name>/create/', views.ContentCreateUpdateView.as_view(),name='module_content_create'), # content create
    path('module/<int:module_id>/content/<model_name>/<id>/', views.ContentCreateUpdateView.as_view(),name='module_content_update'),# content update
    path('content/<int:id>/delete/', views.ContentDeleteView.as_view(), name='module_content_delete'), # content delete
    path('module/<int:module_id>/', views.ModuleContentListView.as_view(), name='module_content_list'),


    # Displaying
    path('',views.CourseListView.as_view(), name='course_list_view'),
    path('subject/<slug:subject>/', views.CourseListView.as_view(), name='course_subject_list_view'),
    path('<slug:slug>/', views.CourseDetailView.as_view(), name='course_detail_view')

]

