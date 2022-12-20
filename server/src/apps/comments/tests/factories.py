import factory
from faker import Faker
fake = Faker()

from apps.books.models import Books


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Books

    title = 'Harry Potter'
    # file = ''
    # genre =
    # slug =
    # cover =
    # created_at =
    author = 'J.K. Rowling'
    # user =








