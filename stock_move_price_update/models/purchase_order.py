# Copyright 2018 Carlos Dauden - Tecnativa <carlos.dauden@tecnativa.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models
from odoo.tools.float_utils import float_compare


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    def write(self, vals):
        res = super().write(vals)
        if 'price_unit' in vals and not self.env.context.get(
                'skip_cost_update'):
            self.price_unit_update()
            print('price_unit_update')
        return res

    def price_unit_update(self):
        for line in self:
            if line.state not in ['purchase', 'done']:
                continue
            # TODO: avoid recompute for chained moves
            line.move_ids.write({
                'price_unit': line.price_unit,
            })
