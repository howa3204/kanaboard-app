from django.urls import path

from . import views

app_name = 'tasks'
urlpatterns = [
    path('tasks/', views.tasks, name='tasks'),
    path('add_task/', views.create_task, name='add_task'),
    path('update_task/<int:task_id>/', views.update_task, name='update_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
]
