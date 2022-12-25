from django import forms
from .models import Dweet, Profile
from django.contrib.auth.models import User



class DweetForm(forms.ModelForm):
    body = forms.CharField(required=True , widget=forms.widgets.Textarea(attrs={
        "placeholder": "Dweet something...",
        "class": "textarea is-success is-medium",
    }),label='')

    class Meta:
        model = Dweet
        exclude = ('user',)


class UserUpdateForm(forms.ModelForm):

    email = forms.EmailField()

    def  __init__(self,*args,**kwargs):
        super(UserUpdateForm, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'field control input',
        }),

        self.fields['email'].widget.attrs.update({
            'class': 'field control input',
            "placeholder": "e.g. alex@example.com",
        })

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['image'].widget.attrs.update({
            "placeholder":"myImageField2",
        }),

    class Meta:
        model = Profile
        fields = ['image']

class DweetUpdateForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['body'].widget.attrs.update({
            "class":"textarea",
        }),

    class Meta:
        model = Dweet
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'cols': 40, 'rows': 10}),
        }