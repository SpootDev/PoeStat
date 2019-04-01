# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import TextField, PasswordField, \
    SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length

from .models import User


# new user registration
class RegisterForm(Form):
    username = TextField('Username',
                         validators=[DataRequired(), Length(min=3, max=25)])
    email = TextField('Email',
                      validators=[DataRequired(), Email(), Length(min=6, max=40)])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=6, max=40)])
    confirm = PasswordField('Verify password',
                            [DataRequired(), EqualTo('password', message='Passwords must match')])

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        initial_validation = super(RegisterForm, self).validate()
        if not initial_validation:
            return False
        user = User.query.filter_by(username=self.username.data).first()
        if user:
            self.username.errors.append("Username already registered")
            return False
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append("Email already registered")
            return False
        return True


# for searching
class SearchEditForm(Form):
    # fields
    search_string = TextField("Search string", validators=[DataRequired()])
    search_media_type = SelectField("Media Type", choices=[('any', 'Any'),
                                                           ('video', 'Video'),
                                                           ('audio', 'Audio'),
                                                           ('image', 'Image'),
                                                           ('publication', 'Publication'),
                                                           ('game', 'Game')])
    search_primary_language = SelectField("Language", choices=[('any', 'Any'),
                                                               ('sd', 'SD'),
                                                               ('hd', 'HD'),
                                                               ('uhd', 'UHD')])
    search_secondary_language = SelectField("Subtitle", choices=[('any', 'Any'),
                                                                 ('sd', 'SD'),
                                                                 ('hd', 'HD'),
                                                                 ('uhd', 'UHD')])

    def __init__(self, *args, **kwargs):
        super(SearchEditForm, self).__init__(*args, **kwargs)

    def validate(self):
        initial_validation = super(SearchEditForm, self).validate()
        if not initial_validation:
            return False
        return True
