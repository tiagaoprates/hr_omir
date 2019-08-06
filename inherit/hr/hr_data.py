# -*- coding: utf-8 -*-
from odoo import models, fields


class Employee(models.Model):
    _inherit = 'hr.employee'

    hr_omir_saude_coleta_ids = fields.One2many('hr.omir.saude.coleta', 'hr_employee_id',
                                               'Anotacoes do Paciente')
