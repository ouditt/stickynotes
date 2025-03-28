# notes/test.py
from django.test import TestCase
from django.urls import reverse
from .models import Note, Author

class NoteModelTest(TestCase):
    '''Testing the Note model.'''
    def setUp(self):
        '''Set up the test environment.'''
        # Creating an author
        author = Author.objects.create(name='Test Author')
        # Creating a note for testing  
        Note.objects.create(title='Test Note', content='Test Content', author=author)
    
    def test_note_has_title(self):
        '''Test that the note has a title.'''
        note = Note.objects.get(id=1)
        self.assertEqual(note.title, 'Test Note')
    
    def test_note_has_content(self):
        '''Test that the note has content.'''
        note = Note.objects.get(id=1)
        self.assertEqual(note.content, 'Test Content')
    
    def test_note_has_author(self):
        '''Test that the note has an author.'''
        note = Note.objects.get(id=1)
        self.assertEqual(note.author.name, 'Test Author')
    
class NoteViewTest(TestCase):
    '''Testing the views for the Note model.'''
    def setUp(self):
        '''Set up the test environment.'''
        # Creating an author
        author = Author.objects.create(name='Test Author')
        # Creating a note for testing  
        Note.objects.create(title='Test Note', content='Test Content', author=author)
    
    def test_note_list_view(self):
        '''Test the note list view.'''
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')
    
    def test_note_detail_view(self):
        '''Test the note detail view.'''
        note = Note.objects.get(id=1)
        response = self.client.get(reverse('note_detail', args=[str(note.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')
        self.assertContains(response, 'Test Content')
    
    def test_note_create_view(self):
        '''Test the note create view.'''
        response = self.client.get(reverse('note_create'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Title')
        self.assertContains(response, 'Content')
    
    def test_note_update_view(self):
        '''Test the note update view.'''
        response = self.client.get(reverse('note_update', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Title')
        self.assertContains(response, 'Content')
    