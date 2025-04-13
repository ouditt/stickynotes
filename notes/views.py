# notes/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm


# Create your views here.
def note_list(request):
    '''Display a list of notes
    
    :param request: The request object
    :type request: HttpRequest
    :return: rendered template with a list of notes
    '''
    notes = Note.objects.all()
    
    # creating as context dictionary to pass data
    context = {
        'notes': notes,
        'page_title': 'List of Notes',
    }
    
    return render(request, 'notes/note_list.html', context)

def note_detail(request, pk):
    '''Display details of a note
    
    :param request: The request object
    :type request: HttpRequest
    :param pk: The primary key of the note
    :return: rendered template with the note details
    '''
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'notes/note_detail.html', {'note': note})

def note_create(request):
    '''Create a new note
    
    :param request: The request object
    :type request: HttpRequest
    :return: rendered template with the note form
    '''
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})

def note_update(request, pk):
    '''Edit an existing note
    
    :param request: The request object
    :type request: HttpRequest
    :param pk: The primary key of the note to be updated
    :return: rendered template for updating the specified note
    '''
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form})

def note_delete(request, pk):
    '''Delete an existing note
    
    :param request: The request object
    param pk: The primary key of the note to be deleted
    :return: redirect to the list of notes after deletion
    '''
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('note_list')