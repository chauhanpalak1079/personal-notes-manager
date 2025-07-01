from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm
from django.contrib.auth.decorators import login_required

@login_required
def list_notes(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'notes/list.html', {'notes': notes})

@login_required
def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('list_notes')
    else:
        form = NoteForm()
    return render(request, 'notes/create.html', {'form': form})

#edit_note view to handle editing existing notes
@login_required
def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('list_notes')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/create.html', {'form': form})

#delete_note view to handle deleting notes
@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('list_notes')
    return render(request, 'notes/delete.html', {'note': note})
