# -*- coding: utf-8 -*-

from decimal import ROUND_UP

from flask_wtf import Form
from wtforms import TextField, PasswordField, TextAreaField, BooleanField, SelectField, DecimalField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class BackupEditForm(Form):
    """
    for editing backups
    """
    enabled = BooleanField('Enabled')

    # interval = SelectField('Interval', choices=[('Hours', 'Hours'),\
    # ('Days', 'Days'), ('Weekly', 'Weekly')])
    # time = DecimalField('Time', places = 2, rounding=ROUND_UP)

    def __init__(self, *args, **kwargs):
        super(BackupEditForm, self).__init__(*args, **kwargs)

    def validate(self):
        initial_validation = super(BackupEditForm, self).validate()
        if not initial_validation:
            return False
        return True


class UserEditForm(Form):
    """
    for editing user
    """
    username = TextField('Username',
                         validators=[DataRequired(), Length(min=3, max=25)])
    email = TextField('Email',
                      validators=[DataRequired(), Email(), Length(min=6, max=40)])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=6, max=40)])
    confirm = PasswordField('Verify password',
                            [DataRequired(), EqualTo('password', message='Passwords must match')])
    enabled = BooleanField('Enabled')
    is_admin = BooleanField('Admin')

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)

    def validate(self):
        initial_validation = super(UserEditForm, self).validate()
        if not initial_validation:
            return False
        return True


class AdminSettingsForm(Form):
    """
    for editing user
    """
    servername = TextField('Server Name', validators=[
        DataRequired(), Length(min=3, max=250)])
    servermotd = TextField('Server MOTD', validators=[Length(min=0, max=250)])
    activity_purge_interval = SelectField('Purge Activity Data Older Than',
                                          choices=[('Never', 'Never'), ('1 Day', '1 Day'),
                                                   ('Week', 'Week'), ('Month',
                                                                      'Month'),
                                                   ('Quarter', 'Quarter'), ('6 Months',
                                                                            '6 Months'),
                                                   ('Year', 'Year')])
    user_password_lock = SelectField('Lock account after failed attempts',
                                     choices=[('Never', 'Never'), ('3', '3'), ('5', '5'),
                                              ('10', '10')])
    # language = SelectField('Interval', choices=[('Hours', 'Hours'),
    # ('Days', 'Days'), ('Weekly', 'Weekly')])
    # country = SelectField('Interval', choices=[('Hours', 'Hours'),
    # ('Days', 'Days'), ('Weekly', 'Weekly')])
    docker_pgadmin = BooleanField('Start PgAdmin (database webgui)')
    docker_portainer = BooleanField('Start Portainer (Docker monitor)')
    docker_smtp = BooleanField('Start SMTP (Mail Server)')
    docker_wireshark = BooleanField('Start Wireshark (network sniffer)')

    def __init__(self, *args, **kwargs):
        super(AdminSettingsForm, self).__init__(*args, **kwargs)

    def validate(self):
        initial_validation = super(AdminSettingsForm, self).validate()
        if not initial_validation:
            return False
        return True


class CronEditForm(Form):
    """
    for editing the cron jobs
    """
    name = TextField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    enabled = BooleanField('Enabled')
    interval = SelectField('Interval', choices=[('Minutes', 'Minutes'), ('Hours', 'Hours'),
                                                ('Days', 'Days'), ('Weekly', 'Weekly')])
    time = DecimalField('Time', places=2, rounding=ROUND_UP)
    script_path = TextField('Script Path', validators=[
        DataRequired(), Length(min=1, max=255)])

    def __init__(self, *args, **kwargs):
        super(CronEditForm, self).__init__(*args, **kwargs)

    def validate(self):
        initial_validation = super(CronEditForm, self).validate()
        if not initial_validation:
            return False
        return True
