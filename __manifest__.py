# -*- coding: utf-8 -*-
{
    'name': "Cash register",
    'summary': """
        Registration of income / expenses in the cash register.""",
    'description': """
        Shows the movements made by the contacts, whether they are in/out, and the date on which they were made.
    """,
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Accounting',
    'version': '0.1',
    'depends': ['base', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'application': True,
}
