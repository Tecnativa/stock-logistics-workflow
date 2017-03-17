# -*- coding: utf-8 -*-
# © 2017 Sergio Teruel <sergio.teruel@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Stock Picking Sale Margin",
    "summary": "Update margin in sales order line after picking validation",
    "version": "9.0.1.0.0",
    "category": "Inventory",
    "website": "http://www.tecnativa.com",
    "author": "Tecnativa, "
              "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "account",
        "sale_stock",
    ],
    "data": [
        "views/sale_view.xml",
    ],
    'post_init_hook': 'post_init_hook',
}
