# -*- coding: utf-8 -*-
# from odoo import http


# class CustomerOdoo(http.Controller):
#     @http.route('/customer_odoo/customer_odoo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/customer_odoo/customer_odoo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('customer_odoo.listing', {
#             'root': '/customer_odoo/customer_odoo',
#             'objects': http.request.env['customer_odoo.customer_odoo'].search([]),
#         })

#     @http.route('/customer_odoo/customer_odoo/objects/<model("customer_odoo.customer_odoo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('customer_odoo.object', {
#             'object': obj
#         })
