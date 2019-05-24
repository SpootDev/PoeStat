"""
User view in webapp
"""
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, g, flash, request

blueprint = Blueprint("user_stash", __name__, url_prefix='/users',
                      static_folder="../static")
import sys

sys.path.append('..')
sys.path.append('../..')
from common import common_config_ini
from common import common_pagination
from common import common_search_stash
import database as database_base
from mainapp.user.forms import StashSearchForm

db_connection = common_config_ini.com_config_read()


def flash_errors(form):
    """
    Display each error on top of form
    """
    for field, errors in form.errors.items():
        for error in errors:
            flash("Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))


@blueprint.route("/stashitemlist/<base_uuid>/<subtype_uuid>", methods=['GET', 'POST'])
def stash_item_list(base_uuid, subtype_uuid):
    """
    Display main stash
    """
    form = StashSearchForm(request.form)
    # TODO use selected account
    g.account_uuid = g.db_connection.db_base_account_uuid_by_name('spooticusmaximus')
    if request.method == 'POST':
        if form.validate_on_submit():
            page, per_page, offset = common_pagination.get_page_items()
            # populate the item list
            stash_filter_items = common_search_stash.com_search_stash(
                g.db_connection.db_stash_items_by_account(g.account_uuid, base_uuid, subtype_uuid,
                                                          None, offset, per_page),
                shaper_item=form.search_form_shaper_item.data,
                eldar_item=form.search_form_elder_item.data,
                corrupt_item=form.search_form_corrupt_item.data,
                is_usable=form.search_form_useable_item.data,
                veiled_item=form.search_form_veiled_item.data,
                fractured_item=form.search_form_fractured_item.data,
                synthesized_item=form.search_form_synthesized_item.data,
                number_of_sockets=form.search_form_total_sockets.data,
                number_of_links=form.search_form_total_links.data,
                armor_points=form.search_form_minimum_armor.data,
                es_points=form.search_form_minimum_es.data,
                evasion_points=form.search_form_minimum_evasion.data,
                minimum_ilvl=form.search_form_minimum_ilvl.data,
                fire_rez=form.search_form_fire_resistance.data,
                cold_rez=form.search_form_cold_resistance.data,
                light_rez=form.search_form_lightning_resistance.data,
                chaos_rez=form.search_form_chaos_resistance.data)
        else:
            flash_errors(form)
        # pagination = common_pagination.get_pagination(page=page,
        #                                               per_page=per_page,
        #                                               total=len(stash_filter_items),
        #                                               record_name='Stash Items',
        #                                               format_total=True,
        #                                               format_number=True,
        #                                               )
        # return render_template('users/user_account_stash.html',
        #                        form=StashSearchForm(request.form),
        #                        stash_items=stash_filter_items,
        #                        account_player=g.db_connection.db_base_account_char_return(),
        #                        data_items=g.db_connection.db_item_base_item_tree(),
        #                        page=page,
        #                        per_page=per_page,
        #                        pagination=pagination,
        #                        base_uuid=base_uuid,
        #                        subtype_uuid=subtype_uuid
        #                        )
    page, per_page, offset = common_pagination.get_page_items()
    pagination = common_pagination.get_pagination(page=page,
                                                  per_page=per_page,
                                                  total=g.db_connection.db_stash_items_by_account_count(
                                                      g.account_uuid,
                                                      base_uuid,
                                                      subtype_uuid,
                                                      None),
                                                  record_name='Stash Items',
                                                  format_total=True,
                                                  format_number=True,
                                                  )
    return render_template('users/user_account_stash.html',
                           form=form,
                           stash_items=g.db_connection.db_stash_items_by_account(g.account_uuid,
                                                                                 base_uuid,
                                                                                 subtype_uuid,
                                                                                 None,
                                                                                 offset, per_page),
                           account_player=g.db_connection.db_base_account_char_return(),
                           data_items=g.db_connection.db_item_base_item_tree(),
                           page=page,
                           per_page=per_page,
                           pagination=pagination
                           )


@blueprint.before_request
def before_request():
    """
    Executes before each request
    """
    g.db_connection = database_base.ServerDatabase()
    g.db_connection.db_open()


@blueprint.teardown_request
def teardown_request(exception):  # pylint: disable=W0613
    """
    Executes after each request
    """
    g.db_connection.db_close()
