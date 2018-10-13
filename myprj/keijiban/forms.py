from django import forms

class KakikomiForm(forms.Form):
     name = forms.CharField(max_length=30)
     email = forms.EmailField(required=False)
     body = forms.CharField(widget=forms.Textarea)

     # def clean_body(self):
     #     body = self.cleaned_data['body']
     #     # if(body.find('<') != -l or body.find('>') != -l):
     #     if(body.find('<') != -1 or body.find('>') != -1):
     #         raise forms.ValidationError('Tags are not allowed.')
     #     return body
     def clean_body(self):
        body = self.cleaned_data['body']
        if(body.find('<') != -1 or body.find('>') != -1):
            raise forms.ValidationError("Tags are not allowed.")
        return body
