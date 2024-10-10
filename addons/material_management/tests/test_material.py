from odoo.tests import TransactionCase

class TestMaterial(TransactionCase):

    def setUp(self):
        super(TestMaterial, self).setUp()
        self.supplier = self.env['res.partner'].create({'name': 'Test Supplier'})
        self.material_model = self.env['material']

    # Test untuk membuat material baru
    def test_create_material(self):
        material = self.material_model.create({
            'material_code': 'M001',
            'material_name': 'Cotton Fabric',
            'material_type': 'cotton',
            'material_buy_price': 150,
            'supplier_id': self.supplier.id,
        })
        self.assertEqual(material.material_code, 'M001')

    # Test untuk memperbarui material
    def test_update_material(self):
        material = self.material_model.create({
            'material_code': 'M002',
            'material_name': 'Jeans Fabric',
            'material_type': 'jeans',
            'material_buy_price': 200,
            'supplier_id': self.supplier.id,
        })
        material.write({'material_name': 'Updated Jeans Fabric'})
        self.assertEqual(material.material_name, 'Updated Jeans Fabric')

    # Test untuk menghapus material
    def test_delete_material(self):
        material = self.material_model.create({
            'material_code': 'M003',
            'material_name': 'Fabric',
            'material_type': 'fabric',
            'material_buy_price': 100,
            'supplier_id': self.supplier.id,
        })
        material_id = material.id
        material.unlink()
        self.assertFalse(self.material_model.browse(material_id).exists())

    # Test untuk validasi harga beli
    def test_buy_price_validation(self):
        with self.assertRaises(ValidationError):
            self.material_model.create({
                'material_code': 'M004',
                'material_name': 'Invalid Fabric',
                'material_type': 'fabric',
                'material_buy_price': 50,  # Ini harus memicu error validasi
                'supplier_id': self.supplier.id,
            })
