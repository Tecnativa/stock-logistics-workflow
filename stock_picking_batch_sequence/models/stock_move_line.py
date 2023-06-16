# Copyright 2023 Tecnativa - Carlos Dauden
# License AGPL-3 - See https://www.gnu.org/licenses/agpl-3.0.html

from odoo import fields, models


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    picking_sequence = fields.Integer(related="picking_id.sequence")
