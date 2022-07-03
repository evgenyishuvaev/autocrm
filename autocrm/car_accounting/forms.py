from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Marks, Models, Cars


class AddCar(forms.ModelForm):

    class Meta:
        model = Cars
        fields = '__all__'


class StatisticsForm(forms.Form):
    reg_num = forms.CharField(max_length=9, label='Register number', required=False)
    mark = forms.ModelChoiceField(queryset=Marks.objects.all(),
                                  to_field_name='mark',
                                  label='Mark',
                                  required=False
                                  )
    model = forms.ModelChoiceField(queryset=Models.objects.all(),
                                   to_field_name='model',
                                   label='Model',
                                   required=False
                                   )
    release_year = forms.IntegerField(required=False)
    owner_id = forms.CharField(max_length=150, label='Manager', required=False)
