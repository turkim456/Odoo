from odoo import fields, models


class HospitalMedicalRecord(models.Model):
    _name = 'hospital.medical.record'
    _description = 'Medical Record'

    patient_id = fields.Many2one(
        'hospital.patient',
        string='Patient',
        required=True,
    )

    diagnosis = fields.Char(
        string='Diagnosis',
        required=True,
    )

    visit_date = fields.Date(
        string='Visit Date',
        default=fields.Date.today,
    )
    doctor_notes = fields.Text(
    string='Doctor Notes'
)