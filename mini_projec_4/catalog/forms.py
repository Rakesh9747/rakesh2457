from django import forms
from .models import CreditCard

class CreditCardForm(forms.ModelForm):
    class Meta:
        model = CreditCard
        fields = ['cardholder_name', 'card_number', 'expiry_date', 'cvv']
        widgets = {
            'cvv': forms.PasswordInput(),
        }
