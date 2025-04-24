from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.project_list, name='project_list'),
    path('projects/add/', views.project_create, name='project_create'),
    path('projects/edit/<int:pk>/', views.project_update, name='project_update'),
    path('projects/delete/<int:pk>/', views.project_delete, name='project_delete'),

    path('tasks/', views.task_list, name='task_list'),
    path('tasks/add/', views.task_create, name='task_create'),
    path('tasks/edit/<int:pk>/', views.task_update, name='task_update'),
    path('tasks/delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('calendar/', views.task_calendar_view, name='task_calendar'),
    path('api/tasks/', views.task_json, name='task_json'),
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
    path('tasks/filter/', views.task_filter_view, name='task_filter'),
    path('tasks/update-status/<int:pk>/', views.update_task_status, name='update_task_status'),
]