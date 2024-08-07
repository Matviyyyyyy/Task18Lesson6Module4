from django.urls import path
from noting import views

urlpatterns = [
    path("", views.NoteListView.as_view(), name = "note-list"),
    path("<int:pk>/", views.NoteDetailView.as_view(), name= "note-detail"),
    path("add-note/", views.add_note, name="add-note"),
]

app_name = "notes"