# Copyright 2024 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    def _get_lot_sequence(self):
        """Next lot name from the lot sequence of the product, the one Odoo
        uses for its custom lot prefixes, or the general lot sequence"""
        self.ensure_one()
        sequence = self.product_id.lot_sequence_id
        if sequence:
            return sequence.next_by_id()
        return self.env["ir.sequence"].next_by_code("stock.lot.serial")
