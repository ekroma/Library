
from django.db import models

from .utils import get_time
from slugify import slugify
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class Books(models.Model):
    title = models.CharField('Title', max_length=200)
    file = models.FileField(
        'book_file', 
        upload_to='book_file',
        )
    genre = models.ManyToManyField(
        to='Genre',
        related_name='genre'
    )
    slug = models.SlugField('Slug', max_length=220, primary_key=True, blank=True)
    cover = models.ImageField(
        upload_to='book_cover',        
    )
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField('Author', max_length=100, blank=True)
    user = models.ForeignKey(
        verbose_name='Автор',
        to=User,
        on_delete=models.CASCADE,
        related_name='book',
    )

    def save(self, *args, **kwargs):
        if not self.author:
            self.author = self.user.username
        if not self.slug:
            self.slug = slugify(self.title + get_time())
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("book-detail", kwargs={"pk": self.pk})


class BookCover(models.Model):
    image = models.ImageField(upload_to='book_cover')
    book = models.ForeignKey(
        to=Books,
        on_delete=models.CASCADE,
        related_name='book_cover'
    )


class Genre(models.Model):
    name = models.SlugField(primary_key=True, max_length=35)

    def __str__(self):
        return self.name

