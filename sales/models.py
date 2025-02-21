from django.db import models
from books.models import Book # need to connect 'sales' with 'books'

# Create your models here.
class Sale(models.Model):
  book = models.ForeignKey(Book, on_delete = models.CASCADE)
  quantity = models.PositiveIntegerField()
  price = models.FloatField()
  date_created = models.DateTimeField (auto_now_add = True)
  date_created = models.DateTimeField (blank = True)

  def __str__(self):
    return f'id: {self.id}, book: {self.book.name}, quantity: {self.quantity}'