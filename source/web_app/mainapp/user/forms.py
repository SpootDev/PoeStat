# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import TextField, PasswordField, SelectField, BooleanField
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


class StashSearchForm(Form):
    """
    for editing search
    """
    search_form_shaper_item = BooleanField('Is Shaper')
    search_form_elder_item = BooleanField('Is Elder')
    search_form_total_sockets = SelectField('Min Sockets', coerce=int,
                                            choices=[(0, '0'),
                                                     (1, '1'),
                                                     (2, '2'),
                                                     (3, '3'),
                                                     (4, '4'),
                                                     (5, '5'),
                                                     (6, '6')])
    search_form_minimum_armor = TextField('Min Armor', validators=[Length(min=0, max=6)])

    def __init__(self, *args, **kwargs):
        super(StashSearchForm, self).__init__(*args, **kwargs)

    def validate(self):
        initial_validation = super(StashSearchForm, self).validate()
        if not initial_validation:
            return False
        return True
