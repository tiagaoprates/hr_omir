# -*- coding: utf-8 -*-
from odoo import models, api
from odoo.exceptions import ValidationError


class HROmirSaudeColeta(models.Model):
    _inherit = 'hr.omir.saude.coleta'

    @api.model
    def search(self, args):
        args.append(('create_uid', '=', self._uid))
        res = super(HROmirSaudeColeta, self).search(args)
        return res

    @api.model
    def default_get(self, fields_list):
        res = super(HROmirSaudeColeta, self).default_get(fields_list)
        hr_employee_ids = self.env['hr.employee'].search([('user_id', '=', self._uid)])
        if not hr_employee_ids:
            raise ValidationError('Paciente nao cadastrado!')
        res.update({'hr_employee_id': hr_employee_ids[0]})
        return res

