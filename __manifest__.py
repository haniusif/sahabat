# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Sahabat Conf',
   
    'version': '1.0',
    'category': 'Automatically',
     'author': 'Clouds CO',
    'description': """
Sahabat Conf
==================================================
    Sahabat Conf is modules to Create and configure automatically your Odoo " sahabat ERP" database
    and instal the depends modules .
    """,
    'summary': 'ERP  , configure , database , depends modules  ',
    'website': 'https://www.clouds.sd',
    'depends': ['sale','crm','mass_mailing','account','stock'],
 
    'installable': True,
    'auto_install': False,
    'application': True,
    'version' : '0.1',
    'sequence': 1,  
}
