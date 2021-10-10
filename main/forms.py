from django import forms
from .models import *

# Infra add form


class InfraForm(forms.ModelForm):
    class Meta:
        model = Infra
        fields = ('name', 'owner', 'description', 'image', 'electricity', 'railways', 'bridges', 'tunnels', 'water_supply',
                  'sewers', 'telecommunication', 'market', 'transportation', 'distributors', 'suppliers', 'mining_area', 'forest_area', 'ready_to_use_land')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("comment", "rating")
