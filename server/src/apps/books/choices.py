from django.utils.translation import gettext_lazy as _
from django.db import models


class BookStateChoices(models.TextChoices):
    READED = 'READED', _('')
    READ_NOW = 'READ_NOW', _('')
    PLANNIG = 'PLANNING', _('')
