from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from services import StileFormMixin
from users.models import User


class UserRegisterForm(StileFormMixin, UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class NewPasswordForm(StileFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)


class UserForm(StileFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'phone',)

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()
