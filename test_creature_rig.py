import unittest
from src.rigging.creature_rig import CreatureRig

class TestCreatureRig(unittest.TestCase):

    def setUp(self):
        self.creature_rig = CreatureRig()

    def test_create_bones(self):
        # Test the create_bones method
        result = self.creature_rig.create_bones()
        self.assertTrue(result)  # Assuming the method returns True on success

    def test_set_skin_weights(self):
        # Test the set_skin_weights method
        result = self.creature_rig.set_skin_weights()
        self.assertTrue(result)  # Assuming the method returns True on success

if __name__ == '__main__':
    unittest.main()