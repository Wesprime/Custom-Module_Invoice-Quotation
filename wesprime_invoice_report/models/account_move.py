# -*- coding: utf-8 -*-

import base64
import io

import qrcode

from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    def get_wesprime_invoice_qr_data_uri(self):
        self.ensure_one()
        base_url = self.env["ir.config_parameter"].sudo().get_param("web.base.url")
        invoice_url = "%s/web#id=%s&model=account.move&view_type=form" % (base_url, self.id)

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=4,
            border=2,
        )
        qr.add_data(invoice_url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        qr_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

        return "data:image/png;base64,%s" % qr_base64
