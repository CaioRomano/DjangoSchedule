from django.urls import path
from . import views


app_name = 'scheduleapp'


urlpatterns = [
    path('', views.list_schedules, name='list'),
    path('create/', views.create_schedule, name='create'),
    path('edit/<pk>/', views.edit_schedule, name='edit'),
    path('delete/<pk>/', views.delete_schedule, name='delete')
]