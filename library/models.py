from django.db import models

class Library(models.Model):
    book_id=models.CharField(max_length=5, primary_key=True)
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    isbn=models.CharField(max_length=50)
    quantity=models.PositiveIntegerField()


    def __str__(self):
        return self.title