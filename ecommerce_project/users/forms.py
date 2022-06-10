from django import forms
from allauth.account.forms import SignupForm, LoginForm
from .models import User


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class CustomSignupForm(SignupForm):
    '''This is the CustomSignupForm class.

    It extends SignupForm from allauth forms and modifies it to our user signup.
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget = forms.EmailInput(attrs={
            'placeholder': 'Enter e-mail',
            'class': 'form-control'
        })
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'placeholder': 'Enter password',
            'class': 'form-control'
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'placeholder': 'Enter password again',
            'class': 'form-control'
        })

    field_order = ['email', 'name', 'gender',
                   'date_of_birth', 'address', 'password1', 'password2']

    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(
        attrs={
            'class': 'form-control'
        }))
    address = forms.CharField(max_length=254, widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter address',
            'class': 'form-control'
        }))
    date_of_birth = forms.DateField(widget=forms.DateInput(
        attrs={
            'placeholder': 'YYYY-MM-DD',
            'class': 'form-control'
        }))
    name = forms.CharField(max_length=254, widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter fullname',
            'class': 'form-control'
        }))

    def save(self, request):
        '''This function is called during signup to save user data.

        It calls the save method of parent class and then inserts our user entered data.
        '''
        print("CHECK THIS OUT")
        print(request.get_full_path)
        user = super(CustomSignupForm, self).save(request)
        user.email = self.cleaned_data["email"]
        user.gender = self.cleaned_data["gender"]
        user.address = self.cleaned_data["address"]
        user.date_of_birth = self.cleaned_data["date_of_birth"]
        user.name = self.cleaned_data["name"]
        user.user_type = "CUSTOMER"
        user.save()
        return user


class CustomLoginForm(LoginForm):
    '''This is the CustomLoginForm class.

    It extends LoginForm from allauth forms and modifies it to our user login.
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['remember'].widget = forms.HiddenInput()
        self.fields['login'].widget = forms.EmailInput(attrs={
            'placeholder': 'Enter e-mail',
            'class': 'form-control'
        })
        self.fields['password'].widget = forms.PasswordInput(attrs={
            'placeholder': 'Enter password',
            'class': 'form-control'
        })

    def save(self, request):
        '''This is save method.

        It is called on user login.
        '''
        user = super(CustomLoginForm, self).save(request)
        return user


class UpdateUserDetails(forms.ModelForm):
    '''This is the UpdateUserDetails class.

    It extends the ModelForm class for creating a form.
    It updates the user details like gender, address, name and date_of_birth.
    '''
    class Meta:
        '''This is Meta class of UpdateUserDetails class.

        It contains model details and fields of this form.
        '''
        model = User
        fields = ['gender', 'address', 'date_of_birth', 'name']

    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(
        attrs={
            'class': 'form-control'
        }))
    address = forms.CharField(max_length=254, widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter address',
            'class': 'form-control'
        }))
    date_of_birth = forms.DateField(widget=forms.DateInput(
        attrs={
            'placeholder': 'YYYY-MM-DD',
            'class': 'form-control'
        }))
    name = forms.CharField(max_length=254, widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter fullname',
            'class': 'form-control'
        }))


class ShopUserSignUpForm(CustomSignupForm):
    '''This is the ShopUserSignUpForm.

    It extends the CustomSignupForm and adds more fields to it.
    '''
    shopname = forms.CharField(max_length=254, widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter fullname',
            'class': 'form-control'
        }))
