from django.db import models

class Book(models.Model):
    name = models.TextField(max_length=200)
    aurthor = models.TextField(max_length=200)

    def __str__(self):
        return self.name