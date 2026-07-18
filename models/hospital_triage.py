from odoo import fields, models


class HospitalTriage(models.Model):
    _name = 'hospital.triage'
    _description = 'Triage Category'

    name = fields.Char(required=True)