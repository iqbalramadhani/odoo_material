from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Material(models.Model):
    _name = 'material'
    _description = 'Material Registration'

    # Kolom untuk menyimpan kode material
    material_code = fields.Char(string='Material Code', required=True, unique=True)

    # Kolom untuk menyimpan nama material
    material_name = fields.Char(string='Material Name', required=True)

    # Kolom untuk menyimpan jenis material dengan pilihan dropdown
    material_type = fields.Selection(
        selection=[('fabric', 'Fabric'), ('jeans', 'Jeans'), ('cotton', 'Cotton')],
        string='Material Type',
        required=True
    )

    # Kolom untuk menyimpan harga beli material
    material_buy_price = fields.Float(string='Material Buy Price', required=True)

    # Relasi ke supplier
    supplier_id = fields.Many2one('res.partner', string='Related Supplier', required=True)

    # Validasi untuk memastikan harga beli tidak kurang dari 100
    @api.constrains('material_buy_price')
    def _check_buy_price(self):
        for record in self:
            if record.material_buy_price < 100:
                raise ValidationError("Material Buy Price must be greater than or equal to 100.")
            # endif
        # endfor
    # endfunction

    @api.model
    def action_cancel(self):
        return {
            'type': 'ir.actions.act_window_close'
        }
