# -*- coding: utf-8 -*-
from odoo import http

# class Tvpromocrm(http.Controller):
#     @http.route('/tvpromocrm/tvpromocrm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tvpromocrm/tvpromocrm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tvpromocrm.listing', {
#             'root': '/tvpromocrm/tvpromocrm',
#             'objects': http.request.env['tvpromocrm.tvpromocrm'].search([]),
#         })

#     @http.route('/tvpromocrm/tvpromocrm/objects/<model("tvpromocrm.tvpromocrm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tvpromocrm.object', {
#             'object': obj
#         })