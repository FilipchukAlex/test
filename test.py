import unittest
import responses
from function import get_json, CustomRequestError


class TestFunction(unittest.TestCase):

    @responses.activate
    def test_get_json_success(self):
        responses.get(
            "http://test_get_json.com",
            status=200,
            body="{}"
        )
        expected = dict
        actual = type(get_json('http://test_get_json.com'))
        self.assertEqual(actual, expected)

    @responses.activate
    def test_get_json_invalid_data(self):
        responses.get(
            "http://test_get_json.com",
            status=200,
            body="some text"
        )
        with self.assertRaises(CustomRequestError) as exception_context:
            get_json('http://test_get_json.com')
        self.assertEqual(str(exception_context.exception), 'Invalid json data')

    @responses.activate
    def test_get_json_invalid_url(self):
        with self.assertRaises(CustomRequestError) as exception_context:
            get_json('http://test_get_json')
        self.assertEqual(str(exception_context.exception), 'Invalid url, connection error, or http error')

    @responses.activate
    def test_get_json_invalid_url_type(self):
        with self.assertRaises(CustomRequestError) as exception_context:
            get_json(2)
        self.assertEqual(str(exception_context.exception), 'Invalid url, connection error, or http error')

    @responses.activate
    def test_get_json_invalid_url_none(self):
        with self.assertRaises(CustomRequestError) as exception_context:
            get_json(None)
        self.assertEqual(str(exception_context.exception), 'Invalid url, connection error, or http error')

    @responses.activate
    def test_get_json_http_error(self):
        responses.get(
            "http://test_get_json.com",
            status=401,
            body='{"error": "some error"}'
        )
        with self.assertRaises(CustomRequestError) as exception_context:
            get_json('http://test_get_json.com')
        self.assertEqual(str(exception_context.exception), 'Invalid url, connection error, or http error')


if __name__ == '__main__':
    unittest.main()

