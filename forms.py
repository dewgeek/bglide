from wtforms import StringField,TextAreaField 
from wtforms import Form
"""from wtforms.fields.recaptcha import RecaptchaField"""
from wtfrecaptcha.fields import RecaptchaField

class contactForm(Form):
    email = StringField('Email')
    msg = TextAreaField('Message')
    recaptcha = RecaptchaField(public_key="6LdUFPESAAAAAPxnU6Dd52HhUl9O63EcjOSKksFU", private_key="6LdUFPESAAAAADbGULOyQ46_UZ0JjyaRjrFFFqEy", secure=True)
