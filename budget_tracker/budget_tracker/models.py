"""Model for Client."""
from django.utils import timezone

from django.db import models


class Cashflow(models.Model):
    """Model for Client."""

    date_added = models.DateTimeField(default=timezone.now)
    expense = models.PositiveSmallIntegerField(default=0)
    income = models.PositiveSmallIntegerField(default=0)
