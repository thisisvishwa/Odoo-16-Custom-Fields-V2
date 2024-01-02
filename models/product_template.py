from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    barcode = fields.Char(string='Barcode')
    standard_price = fields.Float(string='Cost')
    list_price = fields.Float(string='Sale Price')