odoo.define('product_template.ProductTemplateWidget', function (require) {
    'use strict';

    const core = require('web.core');
    const Widget = require('web.Widget');
    const QWeb = core.qweb;

    const ProductTemplateWidget = Widget.extend({
        template: 'product_template_template',
        xmlDependencies: ['/static/src/xml/product_template_templates.xml'],
        init: function(parent, options) {
            this._super(parent, options);
            this.name = options.name;
            this.barcode = options.barcode;
            this.standard_price = options.standard_price;
            this.list_price = options.list_price;
        },
        start: function() {
            this._super();
            this._render();
        },
        _render: function() {
            const $content = $(QWeb.render('product_template_template', {
                name: this.name,
                barcode: this.barcode,
                standard_price: this.standard_price,
                list_price: this.list_price
            }));
            this.$el.html($content);
        }
    });

    core.action_registry.add('product_template_widget', ProductTemplateWidget);

    return ProductTemplateWidget;
});