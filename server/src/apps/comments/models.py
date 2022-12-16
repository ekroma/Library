from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

from apps.books.models import Books

User = get_user_model()


class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField('Body', max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='replies')
    likes = models.ManyToManyField(User, blank=True, related_name='likers')

    class Meta:
        ordering = ('created_at', )
        verbose_name_plural = "Comments"

    def __str__(self):
        return f'Comment by {self.author.username} on {self.book}'

    def count_likes(self):
        if self.likes.count():
            return self.likes.count()
        return 0

    def get_absolute_url(self):
        return reverse("comments-detail", kwargs={"pk": self.id})

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True








