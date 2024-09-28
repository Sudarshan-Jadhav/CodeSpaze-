from django import forms

class ScriptForm(forms.Form):
    url = forms.URLField(label='Website URL', widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter URL to script'}))
