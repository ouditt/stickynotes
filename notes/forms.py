# notes/forms.py
from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    '''A form for creating and updating notes.
    
    fields:
    - title: CharField for the title of the note.
    - content: TextField for the content of the note.
    
    Meta class:
    - Defines the model to use (Note) and the fields to include in the form.
    
    :param forms.ModelForm: Django's ModelForm class.
    '''
    class Meta:
        model = Note
        fields = ['title', 'content', 'author']
        