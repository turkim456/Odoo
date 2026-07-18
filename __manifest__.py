{
    'name': 'Odoo Emergency Triage',
    'depends': ['base', 'mail'],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/hospital_patient_views.xml',
        'views/hospital_doctor_views.xml',
        'views/hospital_menus.xml',
        

        
    ],
}