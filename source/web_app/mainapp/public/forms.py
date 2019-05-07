# -*- coding: utf-8 -*-

from mainapp.user.models import User
from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired


class SearchForm(Form):
    """
    for searching media
    """
    search_text = TextField('Search For')

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)

    def validate(self):
        initial_validation = super(SearchForm, self).validate()
        if not initial_validation:
            return False
        return True
