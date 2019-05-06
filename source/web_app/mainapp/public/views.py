# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""

import sys

sys.path.append('..')
from flask import Blueprint, request, render_template, flash, url_for, redirect, session

blueprint = Blueprint('public', __name__, static_folder="../static")


@blueprint.route("/", methods=["GET", "POST"])
def home():
    """
    Display home page
    """
    redirect_url = request.args.get("next") or url_for("user.members")
    return redirect(redirect_url)


@blueprint.route("/about/")
def about():
    """
    Display about page
    """
    return render_template("public/about.html")
