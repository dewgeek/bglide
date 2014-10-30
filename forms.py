from wtforms import StringField,TextAreaField 
from wtforms import Form
"""from wtforms.fields.recaptcha import RecaptchaField"""
from wtfrecaptcha.fields import RecaptchaField

class contactForm(Form):
    email = StringField('Email')
    msg = TextAreaField('Message')
    recaptcha = RecaptchaField(public_key="xxx", private_key="xxx", secure=True)
