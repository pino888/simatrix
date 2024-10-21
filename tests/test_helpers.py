import unittest

from ..simatrix.matrix import simple_matrix, display_matrix, show_info


class TestSimpleMatrix(unittest.TestCase):
    def test_type(self):
        """
        Test that non list type throws an error
        """
        with self.assertRaises(TypeError):
            simple_matrix(1, 1, 1, "1")


if __name__ == '__main__':
    unittest.main()
