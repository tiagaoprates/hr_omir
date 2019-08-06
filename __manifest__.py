# -*- coding: utf-8 -*-
{
    'name': "Customizacao Omir",

    'summary': """Modulo de integracao ao RH do ODOO.""",

    'description': """
        Customizacao ao modulo RH ODOO
    """,

    'author': "Tiago Prates",

    'category': 'Human Resources',
    'version': '1.0',

    'depends': ['hr'],

    'data': [
        'views/hr_omir_saude_coleta_view.xml',
        'inherit/hr/hr_views.xml',
        'views/action.xml',
        'views/menu.xml',
        'security/bcy_group.xml',
        'security/ir.model.access.csv',
    ],
    'application': True,
}
