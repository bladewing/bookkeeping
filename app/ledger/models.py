from django.contrib.auth import get_user_model
from django.db import models
from djmoney.models.fields import MoneyField


class Entry(models.Model):
    name = models.CharField(max_length=200)
    price = MoneyField(decimal_places=2, default=0, default_currency='EUR', max_digits=11)
    comment = models.TextField(blank=True)
    paid_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RecurringEntry(Entry):
    start = models.DateField()
    end = models.DateField(null=True)
    recurrence = models.DurationField()


class SingleEntry(Entry):
    date = models.DateField()
