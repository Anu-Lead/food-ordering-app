from django import forms
from .models import Pizza, Size


class PizzaForm(forms.ModelForm):
    email = forms.EmailField()
    address = forms.Textarea()
    phone_no = forms.IntegerField()
    swallow = forms.ChoiceField()

    class Meta:
        model = Pizza
        fields = ['swallow', 'soup', 'size', 'address']
        labels = {'swallow': 'Swallow', 'soup': 'Soup', 'address': 'Address'}


class MultiplePizzaForm(forms.Form):
    number_of_plates = forms.IntegerField(min_value=2, max_value=100)

