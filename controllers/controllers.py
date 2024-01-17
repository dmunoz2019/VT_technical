# -*- coding: utf-8 -*-
# from odoo import http


# class DeplogProjectExt(http.Controller):
#     @http.route('/deplog_project_ext/deplog_project_ext', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/deplog_project_ext/deplog_project_ext/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('deplog_project_ext.listing', {
#             'root': '/deplog_project_ext/deplog_project_ext',
#             'objects': http.request.env['deplog_project_ext.deplog_project_ext'].search([]),
#         })

#     @http.route('/deplog_project_ext/deplog_project_ext/objects/<model("deplog_project_ext.deplog_project_ext"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('deplog_project_ext.object', {
#             'object': obj
#         })

