from django import forms
from .models import *

# Infra add form
class InfraForm(forms.ModelForm):
    class Meta:
        model = Infra
        fields = ('name', 'director', 'cast', 'description', 'release_date', 'image')
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("comment", "rating")