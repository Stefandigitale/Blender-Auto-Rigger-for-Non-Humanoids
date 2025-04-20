import unittest
from src.rigging.abstract_rig import AbstractRig

class TestAbstractRig(unittest.TestCase):

    def setUp(self):
        self.rig = AbstractRig()

    def test_create_shapes(self):
        # Test the create_shapes method
        result = self.rig.create_shapes()
        self.assertTrue(result)  # Assuming it returns True on success

    def test_define_movement_patterns(self):
        # Test the define_movement_patterns method
        patterns = self.rig.define_movement_patterns()
        self.assertIsInstance(patterns, list)  # Assuming it returns a list of patterns

    def test_apply_modifiers(self):
        # Test the apply_modifiers method
        result = self.rig.apply_modifiers()
        self.assertTrue(result)  # Assuming it returns True on success

if __name__ == '__main__':
    unittest.main()