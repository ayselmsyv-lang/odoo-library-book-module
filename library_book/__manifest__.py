{
    'name':'Library Book',
    'version':'17.0.1.0.0',
    'summary':'my first module',
    'description':'I am aiming to make my first odoo module',
    'category':'Tools',
    'author': 'Aysel',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/book_view.xml',
        'data/demo_data.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
