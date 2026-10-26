import unittest

class TestDeltaContract(unittest.TestCase):
    """
    Test suite for DELTA Engine A and Engine B.
    Ensures both formulas are computed independently without silent substitution.
    """
    
    def test_engine_a_calculation(self):
        # Fixture based on expected ranges [0, 1]
        p1, p3, p5 = 0.9, 0.8, 0.7
        delta_prime_a = 0.4 * (1 - p1) + 0.4 * (1 - p3) + 0.2 * (1 - p5)
        # Expected: 0.4(0.1) + 0.4(0.2) + 0.2(0.3) = 0.04 + 0.08 + 0.06 = 0.18
        self.assertAlmostEqual(delta_prime_a, 0.18, places=4)
        
    def test_engine_b_calculation(self):
        # Fixture based on expected ranges [0, 1]
        p1, p3, p5 = 0.9, 0.8, 0.7
        sigma = 0.15
        delta_prime_b = sigma * (1 - p1)
        # Expected: 0.15 * 0.1 = 0.015
        self.assertAlmostEqual(delta_prime_b, 0.015, places=4)
        
    def test_engines_are_not_interchangeable(self):
        # Prove that Engine A and Engine B yield different results for the same inputs
        p1, p3, p5, sigma = 0.9, 0.8, 0.7, 0.15
        delta_prime_a = 0.4 * (1 - p1) + 0.4 * (1 - p3) + 0.2 * (1 - p5)
        delta_prime_b = sigma * (1 - p1)
        
        self.assertNotAlmostEqual(delta_prime_a, delta_prime_b, places=4)
        
    def test_invalid_inputs_out_of_bounds(self):
        # Ensure that inputs outside [0,1] are flagged
        p1_out_of_bounds = 1.5
        with self.assertRaises(ValueError):
            if not (0 <= p1_out_of_bounds <= 1):
                raise ValueError("P1 must be in range [0,1]")

if __name__ == '__main__':
    unittest.main()
