#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config, get_most_likely_ancestor_consensus, validated_dna_input

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())
    def test_question_a_config(self):
        self.assertEqual(get_most_likely_ancestor_consensus('GATATATGCATATACTT','ATAT'),(2,4,10))
 




