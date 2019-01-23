from django import forms
from testapp.models import reg
class regform(forms.ModelForm):
    class meta:
        model=reg
        widgets={"pwd":forms.PasswordInput()}
        Fields=["user","pwd","fname","lname","dob","mob"]
class loginform(forms.Form):
    user=forms.CharField(max_length=10)
    pwd=forms.CharField(widget=forms.PasswordInput())
