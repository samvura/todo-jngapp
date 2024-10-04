from django.urls import path
from . import views

urlpatterns = [
    #Add task
    path('addTask/', views.addTask, name='addTask'),
    #Mark as done
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    # Mark incomplete
    path('mark_incomplete/<int:pk>/', views.mark_incomplete, name='mark_incomplete'),
    # Edit Feature
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),
    # Delete task
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
]