import unittest
from password_meter import rate_password, _triangle

class TestPasswordMeter(unittest.TestCase):
    def test_empty_is_weak(self):
        value = rate_password('')
        self.assertEqual((value.score, value.label), (0, 'Weak'))

    def test_bounds(self):
        for example in ('a', 'x' * 1000, '12345678', 'SampleDemo42!Only'):
            with self.subTest(example_length=len(example)):
                score = rate_password(example).score
                self.assertGreaterEqual(score, 0)
                self.assertLessEqual(score, 100)

    def test_long_diverse_example_outscores_repetition(self):
        self.assertGreater(rate_password('Demo42!DifferentChars').score, rate_password('aaaaaaaa').score)

    def test_unicode_is_supported(self):
        self.assertIsInstance(rate_password('বাংলাDemo42!').score, int)

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            rate_password(None)

    def test_membership_shape(self):
        self.assertEqual(_triangle(50, 20, 50, 80), 1)
        self.assertEqual(_triangle(20, 20, 50, 80), 0)
        self.assertEqual(_triangle(80, 20, 50, 80), 0)
        for score in (0, 20, 40, 60, 80, 100):
            v = rate_password('x' * score)
            self.assertGreater(max(v.weak_membership, v.medium_membership, v.strong_membership), 0)
            for membership in (v.weak_membership, v.medium_membership, v.strong_membership):
                self.assertGreaterEqual(membership, 0)
                self.assertLessEqual(membership, 1)

if __name__ == '__main__':
    unittest.main()
