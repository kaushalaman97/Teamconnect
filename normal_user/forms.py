from django import forms
from captcha.fields import CaptchaField
from django.contrib.auth.forms import AuthenticationForm

# class CaptchaTestForm(forms.Form):
# 	# myfield = AnyOtherField()
# 	captcha = CaptchaField()


class LoginForm(AuthenticationForm):
	captcha = CaptchaField()