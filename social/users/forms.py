from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'field control input',
        }),

        self.fields['password1'].widget.attrs.update({
            'class': 'field control input',
            "placeholder": "********",
        }),
        self.fields['password2'].widget.attrs.update({
            'class': 'field control input',
            "placeholder": "********",

        }),

        self.fields['email'].widget.attrs.update({
            'class': 'field control input',
            "placeholder": "e.g. alex@example.com",
        })

    class Meta:
        model = User
        fields = ['username','email','password1', 'password2']
        # widgets = {'password1': forms.widgets.PasswordInput(attrs={'class':'field control input',"placeholder" : "********"})}
                
