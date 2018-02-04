import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_first_not_repeating_char(self):
        self.assertEqual(solution.first_not_repeating_char("ybcccccccccccccb"), "y")
        self.assertEqual(solution.first_not_repeating_char("abaabac"), "c")
        self.assertEqual(solution.first_not_repeating_char("abcdefghijklmnopqrstuvwxyziflskecznslkjfabe"), "d")
        self.assertEqual(solution.first_not_repeating_char("abacabaabacaba"), "_")

if __name__ == "__main__":
    unittest.main()
