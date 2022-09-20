from django import forms

# Reordering Form and class-based View

class PositionForm(forms.Form):
    position = forms.CharField()
