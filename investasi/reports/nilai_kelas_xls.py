from odoo import models


class NilaiXlsx(models.AbstractModel):
    _name = 'report.electronics_shop.report_nilai_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
            format1 = workbook.add_format({'font_size': 14, 'align': 'vcenter', 'bold': True})
            sheet = workbook.add_worksheet('Nilai Kelas')
            sheet.write(2, 2, 'name', format1)
            sheet.write(2, 3, lines.name, format1)
            sheet.write(3, 2, 'tahun ajaran', format1)
            sheet.write(3, 3, lines.tahun_ajaran, format1)
           