from django import forms 

class usersForm(forms.Form):
        name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
        phone = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))
        email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
        message = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control","rows":"5"}))