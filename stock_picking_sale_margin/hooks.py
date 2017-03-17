# -*- coding: utf-8 -*-
# © 2017 Sergio Teruel <sergio.teruel@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).


def post_init_hook(cr):
    """
    Updates existing codes matching the default '/' or
    empty. Primarily this ensures installation does not
    fail for demo data.
    :param cr: database cursor
    :return: void
    """
    sql = """
    UPDATE stock_quant sq_up SET cost=(
        SELECT DISTINCT ail.price_unit FROM stock_quant sq
            LEFT JOIN stock_quant_move_rel sqmr ON sqmr.quant_id=sq.id
            LEFT JOIN stock_move sm ON sqmr.move_id=sm.id
            LEFT JOIN purchase_order_line pol ON sm.purchase_line_id=pol.id
            LEFT JOIN account_invoice_line ail ON pol.id=ail.purchase_line_id
        WHERE sm.purchase_line_id IS NOT null and sq.id=sq_up.id
    )
    """
    cr.execute(sql)
