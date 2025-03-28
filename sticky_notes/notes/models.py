from django.db import models

# Create your models here.
class Note(models.Model):
    '''A model representing a note
    
    Attributes:
    - title (str): The title of the note
    - content (str): The content of the note
    - created_at (datetime): The date and time the note was created
    
    Relationships:
    - author: ForeignKey representing the user who created the note
    
    Methods:
    - __str__(): Returns the title of the note as a string
    
    :param models.Model: Django's base model class
    '''
    
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Define a ForeignKey for the author's relationship
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.title


class Author(models.Model):
    '''A model representing an author of the notes
    
    Attributes:
    - name: CharField for the name of the user
    
    Methods:
    - __str__(): Returns the username of the user as a string
    
    :param models.Model: Django's base model class
    '''
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name