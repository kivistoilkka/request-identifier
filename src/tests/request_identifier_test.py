import unittest
from src.request_identifier import RequestIdentifier

class TestRequestIdentifier(unittest.TestCase):
    def setUp(self):
        self.identifier = RequestIdentifier('visma-identity://login?source=severa')

    def test_class_is_created(self):
        self.assertIsInstance(self.identifier, RequestIdentifier)

    def test_request_identifier_object_can_be_created_with_valid_login_uri(self):
        login_identifier = RequestIdentifier('visma-identity://login?source=severa')
        self.assertEqual(login_identifier.path, 'login')
        self.assertEqual(
            login_identifier.parameters,
            { 'source': 'severa' }
        )

    def test_request_identifier_object_can_be_created_with_valid_confirm_uri(self):
        confirm_identifier = RequestIdentifier(
            'visma-identity://confirm?source=netvisor&paymentnumber=102226'
        )
        self.assertEqual(confirm_identifier.path, 'confirm')
        self.assertEqual(
            confirm_identifier.parameters,
            {
                'source': 'netvisor',
                'paymentnumber': 102226
            }
        )

    def test_request_identifier_object_can_be_created_with_valid_sign_uri(self):
        sign_identifier = RequestIdentifier(
            'visma-identity://sign?source=vismasign&documentid=105ab44'
        )
        self.assertEqual(sign_identifier.path, 'sign')
        self.assertEqual(
            sign_identifier.parameters,
            {
                'source': 'vismasign',
                'documentid': '105ab44'
            }
        )

    def test_uri_parser_accepts_valid_login_uri(self):
        result = self.identifier.parse_and_validate_uri(
            'visma-identity://login?source=severa'
        )
        self.assertEqual(
            result,
            {
                'path': 'login',
                'parameters': {
                    'source': 'severa'
                }
            }
        )

    def test_uri_parser_accepts_valid_confirm_uri(self):
        result = self.identifier.parse_and_validate_uri(
            'visma-identity://confirm?source=netvisor&paymentnumber=102226'
        )
        self.assertEqual(
            result,
            {
                'path': 'confirm',
                'parameters': {
                    'source': 'netvisor',
                    'paymentnumber': 102226
                }
            }
        )

    def test_uri_parser_accepts_valid_sign_uri(self):
        result = self.identifier.parse_and_validate_uri(
            'visma-identity://sign?source=vismasign&documentid=105ab44'
        )
        self.assertEqual(
            result,
            {
                'path': 'sign',
                'parameters': {
                    'source': 'vismasign',
                    'documentid': '105ab44'
                }
            }
        )

    def test_uri_parser_do_not_accept_uri_with_invalid_uri_scheme(self):
        with self.assertRaises(ValueError) as cm:
            self.identifier.parse_and_validate_uri('visma://login?source=severa')
        self.assertEqual(str(cm.exception), 'Invalid URI scheme: visma')

    def test_uri_parser_do_not_accept_uri_with_invalid_path(self):
        with self.assertRaises(ValueError) as cm:
            self.identifier.parse_and_validate_uri(
                'visma-identity://logout?source=severa'
            )
        self.assertEqual(str(cm.exception), 'Invalid path: logout')

    def test_uri_parser_do_not_accept_login_uri_with_missing_source_parameter(self):
        with self.assertRaises(ValueError) as cm:
            self.identifier.parse_and_validate_uri('visma-identity://login?')
        self.assertEqual(str(cm.exception), 'Parameters missing')

    def test_uri_parser_do_not_accept_login_uri_with_wrong_parameters(self):
        with self.assertRaises(ValueError) as cm:
            self.identifier.parse_and_validate_uri(
                'visma-identity://login?paymentnumber=102226'
            )
        self.assertEqual(str(cm.exception), 'Missing parameter: source')

    def test_uri_parser_do_not_accept_login_uri_with_too_many_parameters(self):
        with self.assertRaises(ValueError) as cm:
            self.identifier.parse_and_validate_uri(
                'visma-identity://login?source=severa&paymentnumber=102226'
            )
        self.assertEqual(
            str(cm.exception),
            'Too many parameters: source=severa&paymentnumber=102226'
        )

    def test_uri_parser_do_not_accept_confirm_uri_with_invalid_parameter_type(self):
        with self.assertRaises(ValueError) as cm:
            self.identifier.parse_and_validate_uri(
                'visma-identity://confirm?source=netvisor&paymentnumber=aaa226'
            )
        self.assertEqual(str(cm.exception),
            "Invalid parameter type: value for paymentnumber is not <class 'int'>"
        )

    def test_uri_parser_do_not_accept_sign_uri_with_missing_documentid_parameter(self):
        with self.assertRaises(ValueError) as cm:
            self.identifier.parse_and_validate_uri(
                'visma-identity://sign?source=vismasign'
            )
        self.assertEqual(str(cm.exception),
            'Missing parameter: documentid'
        )


    def test_parameter_parser_works_with_valid_input_for_login(self):
        result = self.identifier.parse_parameters("source=severa")
        self.assertEqual(result, { 'source': 'severa' })

    def test_parameter_parser_do_not_accept_empty_parameters(self):
        with self.assertRaises(ValueError) as cm:
            self.identifier.parse_parameters('')
        self.assertEqual(str(cm.exception), 'Parameters missing')

    def test_parameter_parser_do_not_accept_invalid_parameter_name_and_value_pair_only_name(self):
        with self.assertRaises(ValueError) as cm:
            self.identifier.parse_parameters('source')
        self.assertEqual(str(cm.exception), 'Invalid parameter: source')

    def test_parameter_parser_do_not_accept_invalid_parameter_name_and_value_pair_name_and_equal_sign(self):
        with self.assertRaises(ValueError) as cm:
            self.identifier.parse_parameters('source=')
        self.assertEqual(str(cm.exception), 'Invalid parameter: source=')

    def test_parameter_parser_do_not_accept_invalid_parameter_name_and_value_pair_equal_sign_and_value(self):
        with self.assertRaises(ValueError) as cm:
            self.identifier.parse_parameters('=severa')
        self.assertEqual(str(cm.exception), 'Invalid parameter: =severa')

    def test_parameter_parser_do_not_accept_invalid_parameter_name_and_value_pair_only_value(self):
        with self.assertRaises(ValueError) as cm:
            self.identifier.parse_parameters('severa')
        self.assertEqual(str(cm.exception), 'Invalid parameter: severa')
