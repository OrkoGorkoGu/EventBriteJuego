import unittest
from unittest import mock
import Juego

class TestUserInput(unittest.TestCase):
    @mock.patch('Juego.input', create=True)
    def test_get_user_number_bad_input(self, mocked_input):
        mocked_input.side_effect = ["String Text #$%*", "done"]
        test = Juego.get_user_number()
        self.assertEqual(test, "Invalid Input")
    
    @mock.patch('Juego.input', create=True)
    def test_get_user_feedback_ucase_s(self, mocked_input):
        mocked_input.side_effect = ["S", "done"]
        test = Juego.get_user_feedback()
        self.assertEqual(test, "s")    

    @mock.patch('Juego.input', create=True)
    def test_get_user_feedback_ucase_g(self, mocked_input):
        mocked_input.side_effect = ["G", "done"]
        test = Juego.get_user_feedback()
        self.assertEqual(test, "g")
    
    @mock.patch('Juego.input', create=True)
    def test_get_user_feedback_ucase_c(self, mocked_input):
        mocked_input.side_effect = ["C", "done"]
        test = Juego.get_user_feedback()
        self.assertEqual(test, "c")
    
    @mock.patch('Juego.input', create=True)
    def test_get_user_feedback_multiple_chars(self, mocked_input):
        mocked_input.side_effect = ["sgc", "done"]
        test = Juego.get_user_feedback()
        self.assertEqual(test, "Invalid Response")
    
    @mock.patch('Juego.input', create=True)
    def test_get_user_feedback_invalid_choice(self, mocked_input):
        mocked_input.side_effect = ["d", "done"]
        test = Juego.get_user_feedback()
        self.assertEqual(test, "Invalid Response")

class TestNumbers(unittest.TestCase):    
    def test_invalid_range(self):
        test = Juego.generate_number(6,1)
        self.assertEqual(test, "Invalid Range")

    def test_increase_min(self):
        test = Juego.increase_min(33)
        self.assertEqual(test, 34)
        
    def test_decrease_max(self):
        test = Juego.decrease_max(33)
        self.assertEqual(test, 32)
    
if __name__ == '__main__':
   unittest.main()