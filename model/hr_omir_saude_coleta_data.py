# -*- coding: utf-8 -*-
from odoo import models, fields


class HROmirSaudeColeta(models.Model):
    _description = 'Classe de manipulacao dos dados de saude do paciente.'
    _name = 'hr.omir.saude.coleta'

    hr_employee_id = fields.Many2one('hr.employee', 'Paciente')
    glicemia = fields.Integer(string='Glicemia')
    pressao_sistolica = fields.Integer(string='Pressao Sistolica')
    pressao_diastolica = fields.Integer(string='Pressao Diastolica')
    km_de_caminhada = fields.Integer(string='Km de caminhada')
    km_de_corrida = fields.Integer(string='Km de corrida')
