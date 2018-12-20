# -*- coding: utf-8 -*-
{
    'name': "Libros Electronicos",

    'summary': """
        PLE, SUNAT, Account""",

    'description': """
        Libros Electronicos de Compras SUNAT
    """,

    'author': "Grupo YACCK",
    'website': "http://www.grupoyacck.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['l10n_pe_account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/pe_account_le14_view.xml',
        'report/report_le14.xml',
    ],
}