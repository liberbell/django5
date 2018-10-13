from django import forms

class KakikomiForm(forms.Form):
     name = forms.CharField()
     email = forms.EmailField(required=False)
     body = forms.CharField(widget=forms.Textarea)
