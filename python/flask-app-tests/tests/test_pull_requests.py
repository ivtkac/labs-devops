from unittest import TestCase
from unittest.mock import patch, Mock
from requests.exceptions import HTTPError

from handlers.pull_requests import get_pull_requests, HEADERS


# Write your tests here
class TestPullRequests(TestCase):
    @patch("requests.get")
    def test_pull_requests_open(self, get_mock):
        mock_api_data = [
            {
                "title": "Feature: Add useful stuff",
                "number": 56,
                "html_url": "https://github.com/boto/boto3/pull/56",
                "state": "open",
                "user": {"login": "userA"},
            },
            {
                "title": "Bugfix: Fix something",
                "number": 57,
                "html_url": "https://github.com/boto/boto3/pull/57",
                "state": "open",
                "user": {"login": "userB"},
            },
        ]

        expected_output = [
            {
                "title": "Feature: Add useful stuff",
                "num": 56,
                "link": "https://github.com/boto/boto3/pull/56",
            },
            {
                "title": "Bugfix: Fix something",
                "num": 57,
                "link": "https://github.com/boto/boto3/pull/57",
            },
        ]

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_api_data

        get_mock.return_value = mock_response

        state = "open"
        result = get_pull_requests(state)

        expected_api_url = "https://api.github.com/repos/boto/boto3/pulls"
        expected_params = {"state": state, "per_page": 100}

        get_mock.assert_called_once_with(
            expected_api_url, params=expected_params, headers=HEADERS
        )

        self.assertEqual(result, expected_output)

    @patch("requests.get")
    def test_pull_requests_closed_list(self, get_mock):
        mock_api_data = [
            {
                "title": "Merged: Old Feature",
                "number": 1,
                "html_url": "https://github.com/boto/boto3/pull/1",
                "state": "closed",
                "merged_at": "2023-01-01",
            },
            {
                "title": "Closed: Unused Branch",
                "number": 2,
                "html_url": "https://github.com/boto/boto3/pull/2",
                "state": "closed",
                "merged_at": None,
            },
        ]

        expected_output = [
            {
                "title": "Merged: Old Feature",
                "num": 1,
                "link": "https://github.com/boto/boto3/pull/1",
            },
            {
                "title": "Closed: Unused Branch",
                "num": 2,
                "link": "https://github.com/boto/boto3/pull/2",
            },
        ]

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_api_data
        get_mock.return_value = mock_response

        state = "closed"
        result = get_pull_requests(state)

        expected_api_url = "https://api.github.com/repos/boto/boto3/pulls"
        expected_params = {"state": state, "per_page": 100}

        get_mock.assert_called_once_with(
            expected_api_url, params=expected_params, headers=HEADERS
        )

        self.assertEqual(result, expected_output)

    @patch("requests.get")
    def test_pull_requests_empty_list(self, get_mock):
        mock_api_data = []
        expected_output = []

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_api_data
        get_mock.return_value = mock_response

        state = "closed"
        result = get_pull_requests(state)

        self.assertEqual(result, expected_output)
        get_mock.assert_called_once()

    @patch("requests.get")
    def test_pull_requests_api_failure(self, get_mock):
        mock_response = Mock()
        mock_response.status_code = 404

        mock_response.raise_for_status.side_effect = HTTPError(
            "404 Client Error: Not Found for url: ..."
        )

        get_mock.return_value = mock_response

        state = "open"
        with self.assertRaises(HTTPError):
            get_pull_requests(state)

        get_mock.assert_called_once()
