# -*- coding: utf-8 -*-
# © 2016 Carlos Dauden <carlos.dauden@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class StockPickingWave(models.Model):
    _inherit = 'stock.picking.wave'
    
    move_ids = fields.One2many(
        comodel_name='stock.move',
        compute='_compute_move_ids',
        string='Stock moves')

    pack_operation_ids = fields.One2many(
        comodel_name='stock.pack.operation',
        compute='_compute_pack_operation_ids',
        string='Operations')

    pack_operation_product_ids = fields.One2many(
        comodel_name='stock.pack.operation',
        compute='_compute_pack_operation_product_ids',
        inverse=lambda *args, **kwargs: None,
        states={'done': [('readonly', True)], 'cancel': [('readonly', True)]},
        string='Pack operations product')

    pack_operation_pack_ids = fields.One2many(
        comodel_name='stock.pack.operation',
        compute='_compute_pack_operation_pack_ids',
        inverse=lambda *args, **kwargs: None,
        states={'done': [('readonly', True)], 'cancel': [('readonly', True)]},
        string='Pack operations pack')
    
    @api.multi
    @api.depends('picking_ids')
    def _compute_move_ids(self):
        for wave in self:
            wave.move_ids = wave.picking_ids.mapped("move_lines")

    @api.multi
    @api.depends('picking_ids')
    def _compute_pack_operation_ids(self):
        for wave in self:
            wave.pack_operation_ids = wave.picking_ids.mapped(
                'pack_operation_ids')

    @api.multi
    @api.depends('picking_ids')
    def _compute_pack_operation_product_ids(self):
        for wave in self:
            wave.pack_operation_product_ids = wave.picking_ids.mapped(
                'pack_operation_product_ids')

    @api.multi
    @api.depends('picking_ids')
    def _compute_pack_operation_pack_ids(self):
        for wave in self:
            wave.pack_operation_pack_ids = wave.picking_ids.mapped(
                'pack_operation_pack_ids')
