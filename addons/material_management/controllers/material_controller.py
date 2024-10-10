from odoo import http
from odoo.http import request

class MaterialController(http.Controller):

    # Endpoint untuk mendapatkan semua material
    @http.route('/materials', type='http', auth='user', methods=['GET'], csrf=False)
    def get_materials(self, **kwargs):
        materials = request.env['material'].search([])
        return request.render('your_module_name.materials_template', {
            'materials': materials,
        })

    # Endpoint untuk membuat material baru
    @http.route('/materials/create', type='http', auth='user', methods=['POST'], csrf=False)
    def create_material(self, **kwargs):
        material = request.env['material'].create({
            'material_code': kwargs.get('material_code'),
            'material_name': kwargs.get('material_name'),
            'material_type': kwargs.get('material_type'),
            'material_buy_price': float(kwargs.get('material_buy_price')),
            'supplier_id': int(kwargs.get('supplier_id')),
        })
        return request.redirect('/materials')

    # Endpoint untuk memperbarui material
    @http.route('/materials/update/<int:material_id>', type='http', auth='user', methods=['POST'], csrf=False)
    def update_material(self, material_id, **kwargs):
        material = request.env['material'].browse(material_id)
        material.write({
            'material_code': kwargs.get('material_code'),
            'material_name': kwargs.get('material_name'),
            'material_type': kwargs.get('material_type'),
            'material_buy_price': float(kwargs.get('material_buy_price')),
            'supplier_id': int(kwargs.get('supplier_id')),
        })
        return request.redirect('/materials')

    # Endpoint untuk menghapus material
    @http.route('/materials/delete/<int:material_id>', type='http', auth='user', methods=['POST'], csrf=False)
    def delete_material(self, material_id, **kwargs):
        material = request.env['material'].browse(material_id)
        material.unlink()
        return request.redirect('/materials')
