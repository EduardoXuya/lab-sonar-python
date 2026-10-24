import unittest
from operaciones import sumar, restar, multiplicar, dividir
class TestOperaciones(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(3, 2), 5)
        self.assertEqual(sumar(-1, 1), 0)
    def test_restar(self):
        self.assertEqual(restar(10, 5), 5)
    def test_multiplicar(self):
        self.assertEqual(multiplicar(4, 3), 12)
    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)
        with self.assertRaises(ValueError):
            dividir(5, 0)
if __name__ == "__main__":
    unittest.main()
