# -*- coding: utf-8 -*-
# © 2017 Sergio Teruel <sergio.teruel@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def _update_quant_cost(self, cancel_invoice=None):
        for invoice in self.filtered(
                lambda x: x.type in ['in_invoice', 'in_refund']):
            for line in invoice.invoice_line_ids.filtered(
                    lambda x: x.purchase_line_id):
                quants = self.env['stock.move'].search([
                    ('purchase_line_id', '=', line.purchase_line_id.id),
                ]).quant_ids
                quants.write({
                    'cost': line.purchase_line_id.price_unit
                    if cancel_invoice else line.price_unit
                })
                quants.mapped('history_ids').compute_real_margin()

    @api.multi
    def invoice_validate(self):
        res = super(AccountInvoice, self).invoice_validate()
        self._update_quant_cost()
        return res

    @api.multi
    def action_cancel(self):
        res = super(AccountInvoice, self).action_cancel()
        if res:
            self._update_quant_cost(cancel_invoice=True)
        return res
