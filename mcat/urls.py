from django.urls import path

from . import views

app_name = 'mcat'
urlpatterns = [
    path('mcat/', views.mcat, name='mcat'),
    path('add_mcat/', views.create_MCAT, name="add_mcat"),
    path('update_mcat/<int:mcat_id>/', views.update_MCAT, name="update_mcat"),
    path('delete_mcat/<int:mcat_id>/', views.delete_MCAT, name="delete_mcat"),
]
