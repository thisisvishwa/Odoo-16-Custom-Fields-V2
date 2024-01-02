# Installation Guide for Odoo 16 Product Details Module

## Prerequisites
Before you begin the installation of the Product Details Module, ensure that you have the following:
- Odoo 16 Community Edition installed and running.
- Administrative access to the Odoo instance.
- A backup of your Odoo database, in case you need to revert the changes.

## Step 1: Download the Module
Download the module files from the repository or the location provided. The files should include `__manifest__.py`, `models/`, `views/`, `security/`, `data/`, `controllers/`, `static/`, and `tests/` directories, along with the `README.md` and documentation files.

## Step 2: Add the Module to Odoo Addons Path
Copy the downloaded module folder to your Odoo addons directory. The default path is usually `/odoo/addons/`, but it may vary depending on your installation.

## Step 3: Update Module List
Log in to your Odoo instance with administrative rights and navigate to the "Apps" menu. Click on "Update Apps List" to refresh the list of available modules. You may need to remove the "Apps" filter to see all modules if the module does not appear immediately.

## Step 4: Install the Module
In the "Apps" menu, search for 'Product Details Module'. Once you find it, click on the "Install" button to begin the installation process. Odoo will automatically handle the installation and setup of the new module.

## Step 5: Verify Installation
After the installation is complete, navigate to the various integration points such as Purchase Order Lines, Sale Order Lines, and Stock Picking to verify that the new fields (Product Name, Barcode, Cost, and Sale Price) are visible and correctly integrated.

## Troubleshooting
If you encounter any issues during the installation, please refer to the `README.md` file for guidance or check the `doc/technical_documentation.md` for more technical details.

## Support
For further assistance, contact the module developers or the support team. Provide them with the version of the module, Odoo version, and any error logs or messages you have encountered.

Congratulations! You have successfully installed the Product Details Module for Odoo 16 Community Edition. For usage instructions, please refer to the `doc/user_manual.md`.