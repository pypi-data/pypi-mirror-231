import unittest
from unittest.mock import patch
from aiiiSharedPython.module import send_ga_log

class TestSendGaLog(unittest.TestCase):

    def test_missing_client_id(self):
        with self.assertRaises(ValueError) as context:
            send_ga_log("", ["event"], "measurement_id", "api_secret")
        self.assertEqual(str(context.exception), "You need to set your client_id.")

    def test_missing_events(self):
        with self.assertRaises(ValueError) as context:
            send_ga_log("client_id", [], "measurement_id", "api_secret")
        self.assertEqual(str(context.exception), "You need to set your events.")

    def test_missing_measurement_id(self):
        with self.assertRaises(ValueError) as context:
            send_ga_log("client_id", ["event"], "", "api_secret")
        self.assertEqual(str(context.exception), "You need to set your measurement_id.")

    def test_missing_api_secret(self):
        with self.assertRaises(ValueError) as context:
            send_ga_log("client_id", ["event"], "measurement_id", "")
        self.assertEqual(str(context.exception), "You need to set your api_secret.")

    @patch('requests.post')
    def test_send_ga_log_success(self, mock_post):
        mock_response = mock_post.return_value
        mock_response.status_code = 200

        status_code = send_ga_log("client_id", ["event"], "measurement_id", "api_secret")
        self.assertEqual(status_code, 200)

    @patch('requests.post')
    def test_send_ga_log_failure(self, mock_post):
        mock_response = mock_post.return_value
        mock_response.raise_for_status.side_effect = Exception("HTTP Error")

        with self.assertRaises(Exception) as context:
            send_ga_log("client_id", ["event"], "measurement_id", "api_secret")
        self.assertEqual(str(context.exception), "HTTP Error")


if __name__ == '__main__':
    unittest.main()
