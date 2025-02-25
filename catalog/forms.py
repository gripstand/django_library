from django import forms
from .models import Author
from django.forms import ModelForm
from .widgets import DatePickerInput
from bootstrap_datepicker_plus.widgets import DateTimePickerInput

class DateInput(forms.DateInput):
        input_type = 'date'


class AuthorForm(ModelForm):
    class Meta:
        model=Author
        fields=['first_name','last_name','date_of_birth']
        widgets= {
             'date_of_birth':DatePickerInput()
        }
        # if you want to overide labels
        labels={
             'date_of_birth':'DOB'

        }
