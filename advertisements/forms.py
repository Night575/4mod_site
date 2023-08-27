from django import forms
from .models import *
from django.core.exceptions import ValidationError


class AdvertisementModelForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'price', 'auction', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'cols': 60, 'row': 10}),
            'price': forms.NumberInput(attrs={'class': 'form-control-lg'}),
            'auction': forms.CheckboxInput(attrs={'size': 10})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if title.rfind('?') == 0:
            raise ValidationError("Заголовок не может начинаться с ? знака")
        return title


