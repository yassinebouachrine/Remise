# -*- coding: utf-8 -*-
{
    'name': "Gestion des vents et des achats",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Leansoft",
    'website': "http://www.Leansoft.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale','sale_management','base','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/devis_view.xml',
        'views/achat_view.xml',
        'views/facteur_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

}
