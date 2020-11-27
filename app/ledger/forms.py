from bootstrap_datepicker_plus import DatePickerInput
from django import forms

from ledger.models import SingleEntry


class NewSingleEntryForm(forms.ModelForm):
    field_order = ['name', 'price', 'paid_by', 'date', 'comment']

    class Meta:
        model = SingleEntry
        fields = {'name', 'price', 'comment', 'date', 'paid_by'}
        widgets = {
            'date': DatePickerInput(options={'format': 'YYYY-MM-DD', 'debug': True}),
        }
