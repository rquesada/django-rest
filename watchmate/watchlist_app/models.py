from django.db import models

class StreamPlataform(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField(max_length=150)
    webpage = models.TextField(max_length=150)
    
    """
    Method used to represent the object as a string
    """
    def __str__(self):
        return self.name

"""
This class could be Podcast, Movie, or Series, depending on the type of content
"""
class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    activate = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    """
    Method used to represent the object as a string
    """
    def __str__(self):
        return self.title