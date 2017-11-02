# -*- coding: utf-8 -*-
# Copyright 2017 LasLabs Inc.

from odoo import api, SUPERUSER_ID


def post_init_hook(cr, registry):
    """Enable packaging options in stock config."""
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        wizard = env['stock.config.settings'].create({
            'group_stock_packaging': 1,
            'group_stock_tracking_lot': 1,
        })
        wizard.execute()
