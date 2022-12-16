from django.utils.translation import gettext_lazy as _
from django.db import models


class UserBookStateChoices(models.TextChoices):
    HAD_READ = 'read_finished', _('прочитан')
    READING_PROCESS = 'read_process', _('в процессе чтения')
    PLANNING_TO_READ = 'read_planning', _('пранируется к чтению')

