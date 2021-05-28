from django.urls import path

from . import views

app_name = 'activities'
urlpatterns = [
    path('activities/', views.activities, name='activities'),
    path('add_activity/', views.add_activity, name="add_activity"),
    path('update_activity/<int:activity_id>/', views.update_activity, name="update_activity"),
    path('delete_activity/<int:activity_id>/', views.delete_activity, name="delete_activity"),
]
