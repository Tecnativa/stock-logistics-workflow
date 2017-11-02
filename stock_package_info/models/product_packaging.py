# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# Copyright 2015 Serv. Tec. Avanzados - Pedro M. Baeza
# Copyright 2015 AvanzOsc
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class ProductPackaging(models.Model):

    _name = 'product.packaging'
    _inherit = ['product.packaging', 'product.packaging.template']

    product_pack_tmpl_id = fields.Many2one(
        name='Product Package Template',
        comodel_name='product.packaging.template',
    )
    layer_qty = fields.Integer(
        string='Package by Layer',
        help='The number of packages by layer',
    )
    rows = fields.Integer(
        string='Number of Layers',
        required=True,
        default=1,
        help='The number of layers on a pallet or box',
    )
    barcode = fields.Char(
        help='The barcode code of the package unit',
    )
    code = fields.Char(
        help='The code of the transport unit',
    )
    weight = fields.Float(
        string='Total Package Weight',
        help='The weight of a full package, pallet or box',
    )

    @api.onchange('product_pack_tmpl_id')
    def _onchange_product_pack_tmpl_id(self):
        """Update the package fields with that of the template."""

        template = self.product_pack_tmpl_id

        for field_name, field in template._fields.iteritems():

            if not any((
                field.compute, field.related, field.automatic,
                field.readonly, field.company_dependent,
                field.name in self.NO_SYNC,
            )):
                self[field_name] = self.product_pack_tmpl_id[field_name]
