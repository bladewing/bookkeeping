from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from ledger.models import SingleEntry


class DateInput(forms.DateInput):
    input_type = 'date'


class NewSingleEntryForm(forms.ModelForm):
    field_order = ['name', 'price', 'date', 'comment']

    class Meta:
        model = SingleEntry
        fields = {'name', 'price', 'comment', 'date'}
        widgets = {
            'made_on': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
