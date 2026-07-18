from odoo import api, fields, models


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Hospital Doctor'

    name = fields.Char(string='Doctor Name', required=True)

    specialty = fields.Selection(
        selection=[
            ('general', 'General Medicine'),
            ('emergency', 'Emergency Medicine'),
        ],
        string='Specialty',
    )

    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    active = fields.Boolean(string='Active', default=True)

   

    patient_ids = fields.One2many(
        comodel_name='hospital.patient',
        inverse_name='doctor_id',
        string='Assigned Patients',
    )

    patient_count = fields.Integer(
        string='Patients',
        compute='_compute_patient_count',
    )

    @api.depends('patient_ids')
    def _compute_patient_count(self):
        for doctor in self:
            doctor.patient_count = len(doctor.patient_ids)