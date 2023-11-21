from django.urls import path
from . import views as v

urlpatterns=[
    path('', v.getRoutes,name="routes"),
    path('notes/',v.getNotes,name="notes"),
    path('notes/create/',v.createNote,name="create-note"),
    path('notes/<str:pk>/update',v.updateNote,name="update"),
    path('notes/<str:pk>/delete',v.deleteNote,name="delete"),

    path('notes/<str:pk>/',v.getNote,name="note")
]











