# -*- coding: utf-8 -*-
# Copyright 2018 Tecnativa - Sergio Teruel
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openupgradelib import openupgrade


table_renames = [
    ('rel_package_weight_lot',
     'stock_picking_package_weight_lot_stock_production_lot'),
    ('stock_picking_packages_info', 'stock_picking_package_info_ids'),
]


def _rename_module(env):
    """The old name in v8 was stock_picking_package_info"""
    openupgrade.update_module_names(
        env.cr, [
            ('stock_picking_package_info', 'stock_package_info')
        ], merge_modules=True,
    )


@openupgrade.migrate()
def migrate(env, version):
    if not version:
        return
    openupgrade.rename_tables(env.cr, table_renames)
    _rename_module(env)
