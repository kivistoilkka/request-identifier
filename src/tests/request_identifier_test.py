import unittest
from src.request_identifier import RequestIdentifier

class TestRequestIdentifier(unittest.TestCase):
    def setUp(self):
        self.identifier = RequestIdentifier()

    def test_class_is_created(self):
        self.assertIsInstance(self.identifier, RequestIdentifier)
    