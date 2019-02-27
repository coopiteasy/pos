# Copyright 2019 Coop IT Easy SCRLfs
# 	    Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Set Default Product Quantity in POS",
    "version": "9.0.0.1.0",
    "author": "Coop IT Easy SCRLfs, Odoo Community Association (OCA)",
    "website": "www.coopiteasy.be",
    "license": "AGPL-3",
    "category": "Point of Sale",
    "description": """
        When adding an to order line, this module sets the quantity to
         the default quantity set on the product unit category.
    """,
    "depends": [
        'point_of_sale',
    ],
    'data': [
        'views/pos_config.xml',
        'views/product_view.xml',
        'static/src/xml/templates.xml',
    ],
    'installable': True,
}
