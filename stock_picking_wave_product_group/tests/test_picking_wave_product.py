# -*- coding: utf-8 -*-
# © 2016 Carlos Dauden <carlos.dauden@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp.tests.common import TransactionCase
from openerp import fields


class TestPickingWaveProduct(TransactionCase):
    def setUp(self):
        self.partner = self.env['res.partner'].create({
            'name': 'Partner test',
            'customer': True,
        })

    def test_product_group(self):
        pass
