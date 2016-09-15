# -*- coding: utf-8 -*-
# © 2016 Carlos Dauden <carlos.dauden@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Stock Picking Wave Product Group',
    'version': '9.0.1.0.0',
    'category': 'Warehouse',
    'license': 'AGPL-3',
    'author': 'Tecnativa, Odoo Community Association (OCA)',
    'website': 'https://www.tecnativa.com',
    'depends': ['stock_picking_wave'],
    'data': [
        'views/stock_picking_wave_view.xml',
        'wizard/picking_to_wave_view.xml',
    ],
    'installable': True,
}
