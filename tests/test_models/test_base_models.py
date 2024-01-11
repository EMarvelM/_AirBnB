#!/bin/python3

from models.base_model import BaseModel
import unittest

class TestModel(unittest.TestCase):
    def setUp(self):
        self.user = BaseModel()

    def test___init__(self):
        self.assertIsNotNone(self.user.id)
        self.assertIsNotNone(self.user.created_at)
        self.assertIsNotNone(self.user.updated_at)
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test___str__(self):
        val = self.user
        # print(val)
        self.assertIsNotNone(val)

    def test_save(self):
        ck1 = self.user.updated_at
        self.user.save()
        self.assertNotEqual(ck1, self.user.updated_at)

    def test_to_dict(self):
        userdict = self.user.to_dict()
        print(userdict)
        self.assertIn("id", userdict)

if __name__ == "__main__":
    unittest.main()
