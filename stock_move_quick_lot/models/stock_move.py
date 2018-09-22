# Copyright 2018 Carlos Dauden - Tecnativa <carlos.dauden@tecnativa.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class StockMove(models.Model):
    _inherit = 'stock.move'

    lot_name = fields.Char(
        string='Lot Name',
        compute='_compute_lot_name',
        inverse='_inverse_lot_name',
    )
    life_date = fields.Datetime(
        string='End of Life Date',
        help='This is the date on which the goods with this Serial Number may '
             'become dangerous and must not be consumed.',
        compute='_compute_life_date',
        inverse='_inverse_life_date',
    )
    lot_track_enabled = fields.Boolean(
        compute='_compute_lot_track_enabled',
    )

    @api.multi
    def _compute_lot_name(self):
        for line in self:
            line.lot_name = ', '.join(
                lot.name for lot in line.mapped('move_line_ids.lot_id'))

    @api.multi
    def _inverse_lot_name(self):
        for line in self:
            if not line.lot_name:
                continue
            lot = line.production_lot_from_name()
            if not lot:
                lot = lot.create({
                    'name': self.lot_name,
                    'product_id': self.product_id.id,
                    'life_date': self.life_date,
                })
            if line.move_line_ids:
                if line.move_line_ids.lot_id != lot:
                    line.move_line_ids.lot_id = lot
            else:
                print('xxx')
                lot_qty = line.quantity_done or line.product_qty
                move_line_vals = line._prepare_move_line_vals()
                move_line_vals.update({
                    'ordered_qty': line.product_qty,
                    'qty_done': lot_qty,
                    'lot_id': lot.id,
                })
                line.update({
                    'move_line_ids': [(0, 0, move_line_vals)],
                    'quantity_done': lot_qty,
                })

    @api.multi
    @api.depends('product_id', 'lot_name')
    def _compute_life_date(self):
        for line in self:
            if isinstance(line.id, models.NewId):
                lot = self.env['stock.production.lot'].search([
                    ('product_id', '=', self.product_id.id),
                    ('name', '=', self.lot_name),
                ], limit=1)
                line.life_date = lot.life_date
            else:
                line.life_date = line.move_line_ids[:1].lot_id.life_date

    @api.multi
    def _inverse_life_date(self):
        for line in self:
            lot = line.production_lot_from_name()
            if lot and lot.life_date != line.life_date:
                lot.life_date = line.life_date

    @api.multi
    def production_lot_from_name(self):
        StockProductionLot = self.env['stock.production.lot']
        if not self.lot_name:
            if self.move_line_ids:
                raise ValidationError(_('Open detail to remove lot'))
            else:
                return StockProductionLot.browse()
        if len(self.move_line_ids) > 1:
            raise ValidationError(_('Go to lots to change data'))
        lot = StockProductionLot.search([
            ('product_id', '=', self.product_id.id),
            ('name', '=', self.lot_name),
        ], limit=1)
        return lot

    @api.multi
    @api.depends('product_id')
    def _compute_lot_track_enabled(self):
        for line in self:
            line.lot_track_enabled = bool(line.product_id.tracking != 'none')
