import unittest
from src.rigging.mecha_rig import MechaRig

class TestMechaRig(unittest.TestCase):

    def setUp(self):
        self.rig = MechaRig()

    def test_create_joints(self):
        # Test the create_joints method
        result = self.rig.create_joints()
        self.assertTrue(result)  # Assuming the method returns True on success

    def test_set_ik_constraints(self):
        # Test the set_ik_constraints method
        result = self.rig.set_ik_constraints()
        self.assertTrue(result)  # Assuming the method returns True on success

    def test_configure_movement(self):
        # Test the configure_movement method
        result = self.rig.configure_movement()
        self.assertTrue(result)  # Assuming the method returns True on success

if __name__ == '__main__':
    unittest.main()