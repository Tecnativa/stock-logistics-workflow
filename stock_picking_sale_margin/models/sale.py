# -*- coding: utf-8 -*-
# © 2017 Sergio Teruel <sergio.teruel@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    real_cost_price = fields.Float(
        string='Real Cost Price',
        copy=False,
    )
    real_margin = fields.Float(
        compute='_compute_real_margin',
        store=True,
        string='Real margin',
        copy=False,
    )

    @api.multi
    @api.depends('price_unit', 'real_cost_price')
    def _compute_real_margin(self):
        for line in self:
            line.real_margin = line.price_subtotal - (
                line.qty_delivered * line.real_cost_price)
