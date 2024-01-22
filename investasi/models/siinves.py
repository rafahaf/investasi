from datetime import datetime
from odoo import api, fields, models, tools
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT

class userdetails(models.Model):
    _name='user.details'

    name = fields.Many2one('res.users',string="your name",readonly=True,default=lambda self:self.env.user)
    email = fields.Char(string='Email')
    nomor_hp = fields.Char(string='Nomor HP')
    alamat = fields.Char(string='Alamat')
    notaris = fields.Many2one('notaris.details', string='notaris')

class investor(models.Model):
    _name= 'investor.details'
    _description= 'investor'

    name = fields.Char(string='Nama', required=True)
    no_ktp = fields.Char(string='No KTP', required=True)
    email = fields.Char(string='Email', required=True)
    nomor_hp = fields.Char(string='Nomor HP', required=True)
    alamat = fields.Char(string='Alamat')
    company = fields.Char(string='Nama Company')
    linkedin = fields.Char(string='LinkedIn profile')
    notaris = fields.Many2one('notaris.details', string='notaris')
    image = fields.Binary("image")

    
    @api.depends('image')
    def _get_image(self):
        for rec in self:
            rec.image = tools.image_resize_image_medium(rec.image, size=(500, 500))
class bisnis(models.Model):
    _name= 'bisnis.details'
    _description= 'bisnis'

    name = fields.Char(string='Nama', required=True)
    email = fields.Char(string='Email', required=True)
    nomor_hp = fields.Char(string='Nomor HP', required=True)
    alamat = fields.Char(string='Alamat')
    company = fields.Char(string='Nama Company')
    tahun_berdiri = fields.Date('Tahun Didirikan', required=True)
    bidang_bisnis = fields.Selection([('kuliner', 'kuliner'), ('tekstil', 'tekstil'), ('industri', 'industri'), ('perdagangan', 'perdagangan')], 
                                    required=True, string='Bidang Bisnis')
    produk = fields.Char(string='Produk Yang Dibuat')
    penjualan_perbulan = fields.Float(string='Penjualan Perbulan')
    penjualan_pertahun = fields.Float(string='Penjualan Pertahun')
    image = fields.Binary("image")
class notaris(models.Model):
    _name= 'notaris.details'
    _description= 'notaris'

    name = fields.Char(string='Nama', required=True)
    email = fields.Char(string='Email', required=True)
    nomor_hp = fields.Char(string='Nomor HP', required=True)
    alamat = fields.Char(string='Alamat', required=True)
    no_sk = fields.Char(string='No. SK', required=True)
    linkedin = fields.Char(string='LinkedIn profile')
    image = fields.Binary("image")
