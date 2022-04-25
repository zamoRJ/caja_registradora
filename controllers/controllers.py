# -*- coding: utf-8 -*-
# from odoo import http


# class CajaRegistradora(http.Controller):
#     @http.route('/caja_registradora/caja_registradora/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/caja_registradora/caja_registradora/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('caja_registradora.listing', {
#             'root': '/caja_registradora/caja_registradora',
#             'objects': http.request.env['caja_registradora.caja_registradora'].search([]),
#         })

#     @http.route('/caja_registradora/caja_registradora/objects/<model("caja_registradora.caja_registradora"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('caja_registradora.object', {
#             'object': obj
#         })
