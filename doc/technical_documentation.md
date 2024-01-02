# Technical Documentation

## Overview
This document provides a technical overview of the Odoo 16 Community Edition module designed to enhance the visibility of key product details. It covers the data model changes, view customizations, and other technical aspects of the module.

## Data Model Changes
The module extends the `product.template` model to include additional fields for Product Name, Barcode, Cost, and Sale Price. The following fields have been added:

```python
class ProductTemplate(models.Model):
    _inherit = 'product.template'

    barcode = fields.Char(string='Barcode')
    standard_price = fields.Float(string='Cost')
    list_price = fields.Float(string='Sale Price')
```

## View Customizations
The module modifies existing views and adds new ones to display the additional fields. The following views have been updated:

- `views/product_template_views.xml`: Adds the new fields to the product template form, tree, and list views.
- `views/purchase_order_line_views.xml`: Includes the new fields in the purchase order line form view.
- `views/sale_order_line_views.xml`: Includes the new fields in the sale order line form view.
- `views/stock_picking_views.xml`: Includes the new fields in the stock picking form view.

## Security
The module defines access rights for different user roles in `security/ir.model.access.csv` to ensure that only authorized users can access the new fields.

## Controllers
A controller `controllers/main.py` is added to handle HTTP requests related to the product template operations.

## JavaScript Widgets
JavaScript functionality is provided through the `ProductTemplateWidget` defined in `static/src/js/product_template.js`. This widget enhances the user interface by adding interactive elements to the product template views.

## CSS Styling
Custom styles are applied to the new fields and views using the CSS classes defined in `static/src/css/product_template.css`.

## QWeb Templates
Custom QWeb templates are defined in `static/src/xml/product_template_templates.xml` to render the new fields in a user-friendly manner.

## Testing
Unit and integration tests are provided in `tests/test_product_template.py` to ensure the module's functionality works as expected and to prevent regressions.

## Module Structure
The module follows Odoo's modular design principles, with the main configuration specified in `__manifest__.py`. This file includes metadata about the module, such as its name, version, dependencies, data files, and QWeb templates.

## Installation Guide
Refer to `doc/installation_guide.md` for step-by-step instructions on how to install the module.

## User Manual
For detailed usage instructions, including screenshots and usage scenarios, refer to `doc/user_manual.md`.

## Compliance
The module is developed to comply with Odoo's standard development practices and guidelines, ensuring a seamless integration with Odoo 16 Community Edition.