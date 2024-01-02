{
    'name': 'Product Details Enhancement',
    'version': '1.0',
    'summary': 'Enhances visibility of product details in Odoo 16 Community Edition',
    'category': 'Sales',
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'license': 'AGPL-3',
    'depends': ['base', 'sale', 'purchase', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_template_views.xml',
        'data/product_template_data.xml',
        'static/src/xml/product_template_templates.xml',
    ],
    'demo': [],
    'qweb': [
        'static/src/xml/product_template_templates.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}