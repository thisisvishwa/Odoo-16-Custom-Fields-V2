from odoo import http
from odoo.http import request

class ProductTemplateController(http.Controller):

    @http.route('/product_template', type='http', auth='user', website=True)
    def product_template(self, **kw):
        product_templates = request.env['product.template'].search([])
        values = {
            'product_templates': product_templates,
        }
        return request.render('module_name.product_template_template', values)