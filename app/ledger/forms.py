# from bootstrap_datepicker_plus import DatePickerInput
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django import forms
from djmoney.forms import MoneyWidget

from ledger.models import SingleEntry


class SingleEntryCreateAndUpdate(forms.ModelForm):
    field_order = ['name', 'price', 'paid_by', 'date', 'comment']

    class Meta:
        model = SingleEntry
        fields = {'name', 'price', 'comment', 'date', 'paid_by'}
        widgets = {
            'date': DatePickerInput(options={'format': 'YYYY-MM-DD', 'debug': True}),
            'price': MoneyWidget(currency_widget={})
        }
        localized_fields = '__all__'
