from __future__ import unicode_literals

from django import forms
from django.contrib.sites.models import Site

from ...site.models import SiteSettings, AuthorizationKey


class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        exclude = []


class SiteSettingsForm(forms.ModelForm):
    class Meta:
        model = SiteSettings
        exclude = ['site']


class AuthorizationKeyForm(forms.ModelForm):
    class Meta:
        model = AuthorizationKey
        exclude = []
        widgets = {'password': forms.PasswordInput(render_value=True),
                   'key': forms.TextInput(),
                   'site_settings': forms.widgets.HiddenInput()}
