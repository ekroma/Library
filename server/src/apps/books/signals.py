from django.db.models import signals
from django.dispatch import receiver
from .models import Rating


@receiver(signals.post_save, sender=Rating)
def my_handler(sender, instance, **kwargs):
    count, sum = 0, 0

    for rating in  Rating.objects.filter(book=instance.book):
        count += 1
        sum += rating.rating

    # book.rating = sum // count
    # book.save()