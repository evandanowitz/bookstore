from django.db import models
from django.shortcuts import reverse

# Create your models here.

genre_choices = (
  ('classic', 'Classic'),
  ('romantic', 'Romantic'),
  ('comic', 'Comic'),
  ('fantasy', 'Fantasy'),
  ('romantic', 'Romantic'),
  ('horror', 'Horror'),
  ('educational', 'Educational')
)

book_type_choices = (
  ('hardcover', 'Hard cover'),
  ('ebook', 'E-Book'),
  ('audiob', 'Audiobook')
)

class Book(models.Model):
  name = models.CharField(max_length = 120)
  author_name = models.CharField(max_length = 120)
  price = models.FloatField(help_text = 'in US dollars $')
  genre = models.CharField(
    max_length = 12,
    choices = genre_choices,
    default = 'classic'
  )
  book_type = models.CharField(
    max_length = 12,
    choices = book_type_choices,
    default = 'hardcopy'
  )
  # 'customers' refers to a folder named 'customers' that'll be created by Django under the src/media folder
  pic = models.ImageField(upload_to='books', default='no_picture.jpg')

  def __str__(self):
    return str(self.name)
  
  def get_absolute_url(self):
    # The reverse() function returns an absolute path reference (a URL without the domain name) matching a given view and optional parameters.
    return reverse ('books:detail', kwargs={'pk': self.pk})