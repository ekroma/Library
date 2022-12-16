from django.db.models import signals
from django.dispatch import receiver
from .models import UserBookRating


def set_rating(book):
    count = 1
    sum = 1
    for rating in UserBookRating.objects.filter(book=book):
        count += 1
        sum += rating.rating


@receiver(signals.post_save, sender=UserBookRating)
def set_rating(sender, instance, **kwargs):
    count, sum = 0, 0
    book = instance.book

    for rating in UserBookRating.objects.filter(book=book):
        count += 1
        sum += rating.rating
    book.rating = sum / count
    book.save()
