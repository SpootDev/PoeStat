# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""

import os
import sys

sys.path.append('..')
from mainapp.extensions import login_manager
from mainapp.public.forms import LoginForm
from mainapp.user.forms import RegisterForm
from mainapp.user.models import User
from mainapp.utils import flash_errors
from flask import Blueprint, request, render_template, flash, url_for, redirect, session
from flask_login import current_user
from flask_login import login_user, login_required, logout_user
from mainapp.database import (
    Column,
    db,
    Model,
    ReferenceCol,
    relationship,
    SurrogatePK,
)

blueprint = Blueprint('public', __name__, static_folder="../static")


@login_manager.user_loader
def load_user(id):
    return User.get_by_id(int(id))


@blueprint.route("/", methods=["GET", "POST"])
def home():
    """
    Display home page
    """
    form = LoginForm(request.form)
    # Handle logging in
    if request.method == 'POST':
        if form.validate_on_submit():
            login_user(form.user, False)
            flash("You are logged in.", 'success')
            redirect_url = request.args.get("next") or url_for("user.members")
            return redirect(redirect_url)
        else:
            flash_errors(form)
    return render_template("public/home.html", form=form, user=current_user)


@blueprint.route('/logout/')
@login_required
def logout():
    """
    Logout user and clear their session
    """
    logout_user()
    session.clear()
    flash('You are logged out.', 'info')
    return redirect(url_for('public.home'))


@blueprint.route("/register/", methods=['GET', 'POST'])
def register():
    """
    Display registration form
    """
    form = RegisterForm(request.form, csrf_enabled=False)
    if form.validate_on_submit():
        admin_user = False
        # if first user set it as administrator and create if not exists
        if os.path.isfile('/poestat/secure/db.sqlite'):
            pass
        else:
            db.create_all()
            admin_user = True
        # add the user
        new_user = User.create(username=form.username.data,
                               email=form.email.data,
                               password=form.password.data,
                               active=True,
                               is_admin=admin_user)
        flash("Thank you for registering. You can now log in.", 'success')
        return redirect(url_for('public.home'))
    else:
        flash_errors(form)
    return render_template('public/register.html', form=form)


@blueprint.route("/about/")
def about():
    """
    Display about page
    """
    return render_template("public/about.html")
