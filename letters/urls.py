from django.urls import path

from . import views

app_name = 'letters'
urlpatterns = [
    path('letters/', views.letters, name='letters'),
    path('add_letter/', views.create_letter, name="add_letter"),
    path('update_letter/<int:letter_id>/', views.update_letter, name="update_letter"),
    path('delete_letter/<int:letter_id>/', views.delete_letter, name="delete_letter"),
]
