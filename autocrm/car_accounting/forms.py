from django import forms
from .models import Marks, Models, Cars


# class AddCar(forms.Form):
#     reg_num = forms.CharField(max_length=9)
#     mark = forms.ModelChoiceField(queryset=Marks.objects.all(), blank=False)
#     model = forms.ModelChoiceField(queryset=Models.objects.all(), blank=False, to_field_name='model')
#     release_year = forms.DateField()

class AddCar(forms.ModelForm):

    class Meta:
        model = Cars
        fields = '__all__'
