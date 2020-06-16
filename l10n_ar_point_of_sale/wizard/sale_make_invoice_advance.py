##############################################################################
#   Copyright (c) 2018 Eynes/E-MIPS (www.eynes.com.ar)
#   License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
##############################################################################

from odoo import models


class SaleAdvancePaymentInv(models.TransientModel):

    _inherit = "sale.advance.payment.inv"

    def _create_invoice(self, order, so_line, amount):
        invoice = super(SaleAdvancePaymentInv, self)._create_invoice(
            order, so_line, amount)
        denom_id = order.fiscal_position_id.denomination_id
        pos_ar_id = order._get_pos_ar(denom_id)
        invoice.write({
            'denomination_id': denom_id.id,
            'pos_ar_id': pos_ar_id.id,
        })
        return invoice
