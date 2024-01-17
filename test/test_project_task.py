# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase

class TestProjectTask(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super(TestProjectTask, cls).setUpClass()
        cls.Product = cls.env['product.product']
        cls.Partner = cls.env['res.partner']
        cls.Task = cls.env['project.task']

        # Prepare a product and a partner to use in tests
        cls.product = cls.Product.create({'name': 'Test Product'})
        cls.partner = cls.Partner.create({'name': 'Test Partner'})

    def test_field_defaults(self):
        task = self.Task.create({'name': 'Test Task'})
        self.assertEqual(task.type, 'normal', "Default type should be 'normal'")
        self.assertFalse(task.is_international, "Default for is_international should be False")
        self.assertFalse(task.is_security, "Default for is_security should be False")

    def test_field_constraints(self):
        task = self.Task.create({'name': 'Test Task', 'type': 'normal'})
        with self.assertRaises(ValueError):
            task.write({'type': 'invalid_type'})

    def test_many2one_relations(self):
        # Create a new product dynamically
        test_product = self.Product.create({'name': 'Dynamic Test Product'})

        # Create a new partner dynamically
        test_partner = self.Partner.create({'name': 'Dynamic Test Partner'})

        # Create a new task with the dynamically created product and partner
        task = self.Task.create({
            'name': 'Test Task with Dynamic Product',
            'product_id': test_product.id,
            'contact_person_id': test_partner.id
        })

        self.assertEqual(task.product_id, test_product, "Product should be correctly linked to the dynamically created one")
        self.assertEqual(task.contact_person_id, test_partner, "Contact person should be correctly linked to the dynamically created one")
