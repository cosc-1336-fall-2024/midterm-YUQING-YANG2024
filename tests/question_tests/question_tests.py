#write function tests here, don't add input('') statements here!
import unittest
#follow this example to add questions b, c, and d for testing including their functions

from src.question_a.question_a import value_is_prime
from src.question_b.question_b import get_assessment_value, get_tax_assessed
from src.question_c.question_c import reverse_string
from src.question_d.question_d import use_local_variable

class Test_Config(unittest.TestCase):
    #def test_question_a_config(self):
        #self.assertEqual(True, test_config())

#Question a
#2) Test the function with values 4 returns False, 5 returns True, and 11 returns True.
    def test_question_a(self):
        self.assertEqual(False, value_is_prime(4))
        self.assertEqual(True, value_is_prime(5))
        self.assertEqual(True, value_is_prime(11))

#Question b
#2) Write test cases for the functions.
#get_assessment_value with values: 10000 should return 6000, 20000 should return 12000
#get_tax_assessed with values: 6000 should return 43.20, 10000 should return 72
    def test_get_assessment_value(self):
        self.assertEqual(6000, get_assessment_value(10000))
        self.assertEqual(12000, get_assessment_value(20000))
    def test_get_tax_assessed(self):
        self.assertEqual(43.20, get_tax_assessed(6000))
        self.assertEqual(72.00, get_tax_assessed(10000))
  
#Question c
#2) Write the test cases with hello world, the return value should be dlrow olleh. The value hello should return olleh.
    def test_reverse_string(self):
        self.assertEqual("dlrow olleh", reverse_string("hello world"))
        self.assertEqual("poiuytrewq", reverse_string("qwertyuiop"))

#Question d
#2) Write a test case as follows: In the test case function create a variable num with value 100.
#Call the function use_local_variable using the num as the function parameter. Write the test case to show that the values is 100
    def test_local_variable_cant_affect(self):
        num = 100
        use_local_variable(num)
        self.assertEqual(100, num)