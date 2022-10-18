from django.db import models

# Create your models here.
class Note(models.Model):
    day = models.DateField(auto_now=True)
    day_note = models.TextField()

    def __str__(self):
        return f'{self.day}, {self.day_note}'
        