{
    'name': "Deplog Project Extension",
    'version': '1.0',
    'summary': 'Extiende el módulo Project con campos adicionales',
    'sequence': 10,
    'description': """
Deplog Project Extension
========================
Este módulo extiende el modelo 'project.task' en Odoo para agregar campos adicionales como tipo, internacional, producto asociado, seguridad, fecha del proyecto, código del proyecto y persona de contacto.
    """,
    'author': "Diego Alejandro Munoz Del Rio",
    'website': "http://www.tuempresa.com",
    'category': 'Project',
    'depends': ['base', 'project','product'],
    'license': 'AGPL-3',
    'data': [
        'views/project_task_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
