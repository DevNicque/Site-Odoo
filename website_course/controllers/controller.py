from odoo import http


class Course(http.Controller):
    @http.route('/suport', auth='public', website=True)
    def index(self, **kw):
        crm_env = http.request.env['crm.lead']
        oportunidades = crm_env.search([('stage_id.name', '=', 'Qualified')])

        return http.request.render('website_course.index',
                                   {'crm': oportunidades,
                                    'hello': 'Hello world',
                                   })
