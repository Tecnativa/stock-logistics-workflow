# -*- coding: utf-8 -*-
# © 2017 Sergio Teruel <sergio.teruel@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, models


class StockMove(models.Model):
    _inherit = "stock.move"

    @api.multi
    def compute_real_margin(self):
        for move in self.filtered(
                lambda x: x.picking_id.picking_type_code in [
                    'outgoing', 'internal']):
            quants = move.mapped('quant_ids')
            total_cost = 0
            for quant in quants:
                total_cost += quant.qty * quant.cost
            so_lines = move.mapped('procurement_id.sale_line_id').filtered(
                lambda x: x.product_id.invoice_policy in ('order', 'delivery')
            )
            # so_lines = move.mapped('procurement_id.sale_line_id').filtered(
            #     lambda x: x.product_id.invoice_policy in (
            #         'order', 'delivery') and x.product_id.cost_method == 'real'
            # )
            # total_cost = move.product_uom_qty * move.price_unit
            for so_line in so_lines:
                so_line.real_cost_price = total_cost / so_line.qty_delivered
                # so_line.real_cost_price = move.price_unit
                # so_line.real_margin = so_line.price_subtotal - total_cost

    @api.multi
    def action_done(self):
        result = super(StockMove, self).action_done()
        self.compute_real_margin()
        return result
