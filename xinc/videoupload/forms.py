from django import forms

class NameForm(forms.Form):
    file_name = forms.CharField(max_length=100)



