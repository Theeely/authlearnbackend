
from django.urls import path
from . import views

urlpatterns = [
    path("notes/",views.noteCreate.as_view(),name="notes-list"),
    path("notes/delete/<int:pk>/",views.noteDelete.as_view(),name="delete-notes"),
    
]
