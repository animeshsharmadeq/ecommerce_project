from allauth.account.forms import SignupForm, LoginForm
from django import forms
 
class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"] = forms.CharField(max_length=254)
 
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.email = self.cleaned_data['email']
        user.save()
        return user

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['remember'].widget = forms.HiddenInput()

    def save(self, request):
        user = super(CustomLoginForm, self).save(request)
        return user