from django import forms
from .models import *
from django.forms import ModelForm, Textarea
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'comment')
        wisgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15})
        }
