from odoo import fields, models


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'

    name = fields.Char(string='Patient Name ', required=True)
    date_of_birth = fields.Date(string='Date of Birth')

    gender = fields.Selection(
        [
            ('male', 'Male'),
            ('female', 'Female'),
        ],
        string='Gender'
    )

    phone = fields.Char(string='Phone')
    id_number = fields.Char(string='ID' , required=True)
    file_number = fields.Char(string='File Number' , required=True)

    blood_group = fields.Selection(
        [
            ('a+', 'A+'),
            ('a-', 'A-'),
            ('b+', 'B+'),
            ('b-', 'B-'),
            ('ab+', 'AB+'),
            ('ab-', 'AB-'),
            ('o+', 'O+'),
            ('o-', 'O-'),
        ],
        string='Blood Type'
    )

    active = fields.Boolean(default=True)

    doctor_id = fields.Many2one(
        'hospital.doctor',
        string='Assigned Doctor'
    )
    
    medical_record_ids = fields.One2many(
    comodel_name='hospital.medical.record',
    inverse_name='patient_id',
    string='Medical Records',
)

    triage_level = fields.Selection(
    [
        ('critical', 'Critical'),
        ('observation_unit', 'Observation Unit'),
        ('general_ward', 'General Ward'),
        ('opd', 'Outpatient Department (OPD)'),
    ],
    string='Triage Level',
    default='observation_unit'
)