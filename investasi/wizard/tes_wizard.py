
from datetime import datetime
from odoo import api, fields, models
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT

class TesWizard(models.TransientModel):
    _name = 'tes.wizard'
    _description = 'Tes Wizard'


    @api.model
    def default_get(self, fields):
        res = super(TesWizard, self).default_get(fields)
        print("tes context", self._context)
        res['tes_id'] = self._context.get('active_id')
        return res
    # name = fields.Char(string='name', required=True)
    # product_id = fields.Many2one('product.product', string='product id')
    tes_id = fields.Many2one('kelas.details', string='tes')
   

    def create_wizard(self):
       
        self.tes_id.nilai_ids = False
        print('tes button',self.tes_id.nilai_ids)
        
            # tahun_ajaran = fields.Char(string='tahun ajaran')
    # @api.model
    # def default_get(self, field_list):
    #     res = super(TesWizard, self).default_get(field_list)
    #     context = self.env.context
    #     res['tes_id'] = context.get('kelas_details_rec_id', False)
    #     return res
            # for rec in rec.tes_id:
            #     print("tes3")
            
            
    #     self.tahun_ajaran = self.tes_id.tahun_ajaran
    #     print("tahun ajaran", self.tahun_ajaran)
        # context = self.env.context

        # print("tes context",context)
        # for rec in self.tes_id:
        #     print("tahun ajaran", rec.tahun_ajaran)

            