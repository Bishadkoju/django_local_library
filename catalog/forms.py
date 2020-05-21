from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime 

class RenewBookForm(forms.Form):
    renewal_date=forms.DateField(help_text="Enter date form now to 4 weeks (default is 3 weeks).")

    def clean_renewal_date(self):
        data= self.cleaned_data['renewal_date']
        if data<datetime.date.today():
            raise ValidationError('Invalid - Renewal date set to past')
        if data>datetime.date.today()+datetime.timedelta(weeks=4):
            raise ValidationError('Invalid - Renewal date set to more than 4 weeks')
        return data
