from django import forms
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation



# for change the password
class MyPasswordChange(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'currnent_password', 'autofocus': True, 'class': 'input d-inline-block w-100'}))
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new_password', 'class': 'input d-inline-block w-100'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirmm Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new_password', 'class': 'input d-inline-block w-100'}))


# for resettinf the password
class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254, widget=forms.EmailInput(
        attrs={'class': 'input d-inline-block w-100', 'autocomplete': 'email'}))


# for setting the new password
class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_('New Password'), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new_password', 'class': 'input d-inline-block w-100'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_(' Confirm New Password'), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new_password', 'class': 'input d-inline-block w-100'}), help_text=password_validation.password_validators_help_text_html())

