from django import forms

from .models import Reservation


class ReserveTableForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'First Name', 'required': 'required'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'date': forms.DateInput(
                attrs={'class': 'form-control', 'placeholder': 'DD/MM/YYYY', 'required': 'required'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'HH/MM/SS', 'required': 'required'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone', 'required': 'required'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'required': 'required'}),
            'message': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Message'}),

        }
