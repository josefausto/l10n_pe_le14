# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PeAccountConfig(models.Model):
    _inherit = 'pe.account.config'

    type = fields.Selection(selection_add=[('140100', 'Registro de Ventas e Ingresos'), 
                                           ])
    
    