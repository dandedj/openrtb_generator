# FILEPATH: /Users/daviddandeneau/Projects/rtb_generator/openrtb-simulator/tests/test_openrtb_generator.py
import unittest
from chatgpt.OpenRTBGenerator import OpenRTBGenerator

class OpenRTBGeneratorTest(unittest.TestCase):
    def setUp(self):
        self.generator = OpenRTBGenerator()

    def test_generate_request_payload(self):
        request_payload = self.generator.generate_request_payload()
        self.assertIsInstance(request_payload, dict)  # assuming the payload is a dictionary
        # Add more assertions here based on what you expect in the payload

    def test_generate_response_payload(self):
        response_payload = self.generator.generate_response_payload()
        self.assertIsInstance(response_payload, dict)  # assuming the payload is a dictionary
        # Add more assertions here based on what you expect in the payload

if __name__ == '__main__':
    unittest.main()