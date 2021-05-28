from django.urls import path

from . import views

app_name = 'coursework'
urlpatterns = [
    path('coursework/', views.coursework, name='coursework'),
    path('add_course/', views.add_course, name="add_course"),
    path('update_course/<int:course_id>/', views.update_course, name="update_course"),
    path('delete_course/<int:course_id>/', views.delete_course, name="delete_course"),
]
