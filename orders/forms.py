from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email',
                  'address', 'postal_code', 'city']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mt-2'}),
            'address': forms.TextInput(attrs={'class': 'form-control mt-2',
                                              'placeholder': 'Street, apartment, suite, unit etc.'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'city': forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Kyiv'}),
        }
