import re
from datetime import datetime

from django import forms
from django.core.exceptions import ValidationError

from .models import Mark, Model, Car


class AddCar(forms.ModelForm):

    current_year = int(datetime.today().year)

    def clean_reg_num(self):
        # АВЕКМНОРСТУХ - русские буквы
        pattern = r"^[ABEKMHORCTYX]\d{3}(?<!000)[ABEKMHORCTYX]{2}\d{2,3}$"

        reg_num = self.cleaned_data['reg_num']
        if not re.match(pattern, reg_num.upper()):
            raise ValidationError("Invalid format for register number")
        if len(reg_num) < 8:
            raise ValidationError("Register number can't be smaller then 8 or 9 characters")

        return reg_num

    def clean_release_year(self):
        release_year = int(self.cleaned_data['release_year'])
        if release_year > self.current_year:
            raise ValidationError("Release year can't be greater then current year")
        if release_year < 0:
            raise ValidationError("Release year can't be negative value")

        return release_year

    class Meta:
        model = Car
        fields = '__all__'


class StatisticsForm(forms.Form):

    reg_num = forms.CharField(max_length=9, label='Register number', required=False)
    mark = forms.ModelChoiceField(queryset=Mark.objects.all(),
                                  to_field_name='mark',
                                  label='Mark',
                                  required=False
                                  )
    model = forms.ModelChoiceField(queryset=Model.objects.all(),
                                   to_field_name='model',
                                   label='Model',
                                   required=False
                                   )
    release_year = forms.IntegerField(required=False)
    owner_id = forms.CharField(max_length=150, label='Manager', required=False)

