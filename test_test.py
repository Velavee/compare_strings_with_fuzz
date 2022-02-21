import fuzz
import unittest

class Test_TestFuzzyWuzzy(unittest.TestCase):
    # Cases that are expected to be correct
    def test_correct_1(self):
        self.assertEqual(fuzz.check_answer("My name is Gabey.", "My name is Gabey."), True)

    # Cases that are expected to be incorrect
    def test_incorrect_1(self):
        self.assertEqual(fuzz.check_answer("I want to drink beer.", "I want to drink tea."), False)
    
    # Cases that could mistakenly be incorrect
    def test_false_neg_1(self):
        self.assertEqual(fuzz.check_answer("I like apples", "I like apples."), True)

    def test_false_neg_2(self):
        self.assertEqual(fuzz.check_answer("I like apples and bananas.", "I like bananas and apples."), True)

    def test_false_neg_3(self):
        self.assertEqual(fuzz.check_answer("I believe in Santa Claus.", "I beleive in Santa Claus."), True)

    # Cases that could mistakenly be correct
    # This test fails, but that may be unavoidable
    def test_false_pos_1(self):
        self.assertEqual(fuzz.check_answer("Yesterday I received a present.", "Yesterday I receive a present."), False)

    def test_false_pos_2(self):
        self.assertEqual(fuzz.check_answer("I like Daniel.", "Daniel likes me"), False)

    def test_false_pos_3(self):
        self.assertEqual(fuzz.check_answer("The girl likes cats.", "Cats like the girl."), False)

    def test_false_pos_4(self):
        self.assertEqual(fuzz.check_answer("I have a pen.", "I have a pin."), False)

if __name__ == "__main__":
    unittest.main()