# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class ProjectTask(models.Model):
    _inherit = 'project.task'
    _description = 'Project Task Extension'

    type = fields.Selection([
        ('normal', 'Normal'),
        ('abierto', 'Abierto'), 
        ('cerradp', 'Cerrado'),
    ], string='Type', default='normal')
    is_international = fields.Boolean(string='International')
    product_id = fields.Many2one('product.product', string='Product')
    is_security = fields.Boolean(string='Security')
    project_date = fields.Date(string='Project Date')
    project_code = fields.Char(string='Project Code')
    contact_person_id = fields.Many2one('res.partner', string='Contact')
