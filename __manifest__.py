# Copyright 2012 Camptocamp SA - Yannick Vaucher
# Copyright 2017 Tecnativa - Vicent Cubells
# Copyright 2018 brain-tec AG - Raul Martin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Certification',
    'version': '12.0.1.0.0',
    'author': "fatihmd",
    'website': 'https://github.com/OCA/partner-contact',
    'category': 'Customer Relationship Management',
    'license': 'AGPL-3',
    'installable': True,
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/certification_view.xml'
    ],
}
