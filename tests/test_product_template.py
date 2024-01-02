from odoo.tests.common import TransactionCase

class TestProductTemplate(TransactionCase):

    def setUp(self):
        super(TestProductTemplate, self).setUp()
        self.ProductTemplate = self.env['product.template']

    def test_create_product_template(self):
        """Test the creation of a product template with new fields."""
        product_template = self.ProductTemplate.create({
            'name': 'Test Product',
            'barcode': '1234567890123',
            'standard_price': 25.00,
            'list_price': 50.00,
        })
        self.assertTrue(product_template, "Product template was not created.")
        self.assertEqual(product_template.name, 'Test Product')
        self.assertEqual(product_template.barcode, '1234567890123')
        self.assertEqual(product_template.standard_price, 25.00)
        self.assertEqual(product_template.list_price, 50.00)

    def test_update_product_template(self):
        """Test the update of a product template's new fields."""
        product_template = self.ProductTemplate.create({
            'name': 'Test Product',
            'barcode': '1234567890123',
            'standard_price': 25.00,
            'list_price': 50.00,
        })
        product_template.write({
            'name': 'Updated Product',
            'barcode': '9876543210987',
            'standard_price': 30.00,
            'list_price': 60.00,
        })
        self.assertEqual(product_template.name, 'Updated Product')
        self.assertEqual(product_template.barcode, '9876543210987')
        self.assertEqual(product_template.standard_price, 30.00)
        self.assertEqual(product_template.list_price, 60.00)

    def test_unlink_product_template(self):
        """Test the deletion of a product template."""
        product_template = self.ProductTemplate.create({
            'name': 'Test Product',
            'barcode': '1234567890123',
            'standard_price': 25.00,
            'list_price': 50.00,
        })
        product_template_id = product_template.id
        product_template.unlink()
        self.assertFalse(self.ProductTemplate.search([('id', '=', product_template_id)]), "Product template was not deleted.")