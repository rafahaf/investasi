from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSaleInherit(WebsiteSale):
        @http.route([
        '''/shop''',
        '''/shop/page/<int:page>''',
        '''/shop/category/<model("product.public.category", "[('website_id', 'in', (False, current_website_id))]"):category>''',
        '''/shop/category/<model("product.public.category", "[('website_id', 'in', (False, current_website_id))]"):category>/page/<int:page>'''
        ], type='http', auth="public", website=True)
        def shop(self, page=0, category=None, search='', ppg=False, **post):
            res = super(WebsiteSaleInherit, self).shop(page=0, category=None, search='', ppg=False, **post)
            print("Inherited tes ....", res)
            return res

class Investasi(http.controllers):
     
    @http.route('/investor_webform', type="http", auth="public", website=True)
    def investor_webform(self, **kw):
          return http.request.render('investasi.create_investor',{})
    
    @http.route('/create/webinvestor', type="http", auth="public", website=True)
    def create_webinvestor(self, **kw):
        print("Data Received.....", kw)
        request.env['investor'].sudo().create(kw)
        
        return request.render("investasi.patient_thanks", {})