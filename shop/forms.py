from django import forms
from .models import Subscription

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Введіть ваш Email...',
                'style': 'width: 100%; height: 44px; padding: 0 15px; border: 1px solid #ddd; border-radius: 6px; font-size: 14px; box-sizing: border-box;'
            })
        }

# Форма оцінки та відгуку
class ReviewForm(forms.ModelForm):
    class Meta:
        fields = ['name', 'rating', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 100%; padding: 6px; margin-bottom: 10px;'}),
            'rating': forms.Select(attrs={'class': 'form-control', 'style': 'width: 100%; padding: 6px; margin-bottom: 10px;'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'style': 'width: 100%; padding: 6px; margin-bottom: 10px;'}),
        }