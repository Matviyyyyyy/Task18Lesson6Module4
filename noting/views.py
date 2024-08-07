from django.shortcuts import render, redirect
from noting.models import Note
from django.views.generic import ListView, DetailView, CreateView
from noting.forms import NoteForm

class NoteListView(ListView):
    model = Note
    context_object_name = "notes"
    template_name = 'noting/note_list.html'

class NoteDetailView(DetailView):
    model = Note
    context_object_name = "note"
    template_name = 'noting/note_detail.html'

def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes:note-list')
    else:
        form = NoteForm()
    return render(request, 'noting/add_note.html', {'form': form})