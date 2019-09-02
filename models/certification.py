# Copyright 2012 Camptocamp SA - Yannick Vaucher
# Copyright 2018 brain-tec AG - Raul Martin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class Certification(models.Model):
   _name = 'certification'
   _description = 'Certification'

   number = fields.Char()
   date = fields.Date(string='Validation Date')
   description = fields.Text(string='Validation Details')
   standard_id = fields.Many2one("certification.standard")
   owner_id = fields.Many2one("res.partner")
   entity_id = fields.Many2one('res.partner')

