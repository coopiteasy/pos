# -*- coding: utf-8 -*-
# © 2016 Robin Keunen, Coop IT Easy SCRL fs
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from openerp import models, fields, api


class pos_config(models.Model):
    _inherit = 'pos.config'

    set_default_product_quantity = fields.Boolean(
        string='Sets default product quantity in POS',
        default=False,
    )
