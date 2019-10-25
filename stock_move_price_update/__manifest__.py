# Copyright 2018 Tecnativa - Carlos Dauden
# Copyright 2018 Tecnativa - Sergio Teruel
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Stock Move Price Update',
    'summary': 'Set lot name and end date directly on picking operations',
    'version': '11.0.1.0.0',
    'category': 'Stock',
    'website': 'https://github.com/OCA/stock-logistics-workflow',
    'author': 'Tecnativa, Odoo Community Association (OCA)',
    'license': 'AGPL-3',
    'installable': True,
    'depends': [
        'stock_account',
    ],
    'data': [
        'views/stock_view.xml',
    ],
}
