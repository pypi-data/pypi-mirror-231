from github_scraper import *
from unittest.mock import patch, Mock, mock_open, call
import unittest
import os
import sys
sys.path.append(os.getcwd())


class TestGitHubScraper(unittest.TestCase):

    def setUp(self):
        self.token = "test_token"
        self.username = "alice"

    @patch('requests.get')
    def test_fetch_user_profile(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {"login": "alice"}
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        user = GitHubUser(self.username, self.token)
        profile = user.fetch_user_profile()

        self.assertEqual(profile["login"], "alice")

    @patch('requests.get')
    def test_fetch_user_social_accounts(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {
            "provider": "twitter",
            "url": "https://twitter.com/alice"
        }
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        user = GitHubUser(self.username, self.token)
        social_accounts = user.fetch_user_social_accounts()

        self.assertEqual(social_accounts["provider"], "twitter")
        self.assertEqual(social_accounts["url"],
                         "https://twitter.com/alice")

    @patch('requests.get')
    def test_search_users_by_tag(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {
            "items": [
                {"login": "bob"},
                {"login": "charlotte"}
            ]
        }
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        usernames = search_users_by_tag(self.token, "python", 2)
        self.assertEqual(len(usernames), 2)
        self.assertIn("bob", usernames)
        self.assertIn("charlotte", usernames)

    @patch('requests.get')
    def test_fetch_user_profile_404(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        user = GitHubUser(self.username, self.token)
        with self.assertRaises(Exception) as context:
            user.fetch_user_profile()

        self.assertIn("Error fetching profile", str(context.exception))

    @patch('builtins.print')
    def test_check_rate_limit_missing_headers(self, mock_print):
        mock_response = Mock()
        mock_response.headers = {}
        check_rate_limit(mock_response)
        mock_print.assert_called_once_with("Rate limit headers not found!")

    @patch('requests.get')
    def test_scrape_github_user(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {
            "login": "alice", "type": "User"
        }
        mock_response.status_code = 200

        mock_response_social_accounts = Mock()
        mock_response_social_accounts.json.return_value = {}
        mock_response_social_accounts.status_code = 200

        mock_get.side_effect = [mock_response, mock_response_social_accounts]

        data = scrape_github_user(self.token, "alice")
        self.assertEqual(data["login"], "alice")
        self.assertEqual(data["type"], "User")
        self.assertNotIn("social_accounts", data)

    @patch('builtins.print')
    @patch('requests.get')
    @patch('builtins.open', mock_open())
    def test_run_github_scraper(self, mock_get, mock_print):
        mock_response_search = Mock()
        mock_response_search.json.return_value = {
            "items": [
                {"login": "bob"},
                {"login": "charlotte"}
            ]
        }
        mock_response_search.status_code = 200

        mock_response_profile_bob = Mock()
        mock_response_profile_bob.json.return_value = {
            "login": "bob", "type": "User"}
        mock_response_profile_bob.status_code = 200

        mock_response_profile_bob_social_accounts = Mock()
        mock_response_profile_bob_social_accounts.json.return_value = {}
        mock_response_profile_bob_social_accounts.status_code = 200

        mock_response_profile_charlotte = Mock()
        mock_response_profile_charlotte.json.return_value = {
            "login": "charlotte", "type": "User"}
        mock_response_profile_charlotte.status_code = 200

        mock_response_profile_charlotte_social_accounts = Mock()
        mock_response_profile_charlotte_social_accounts.json.return_value = [{
            "provider": "twitter",
            "url": "https://twitter.com/charlotte"
        }]

        mock_response_profile_charlotte_social_accounts.status_code = 200

        mock_get.side_effect = [mock_response_search, mock_response_profile_bob, mock_response_profile_bob_social_accounts,
                                mock_response_profile_charlotte, mock_response_profile_charlotte_social_accounts]

        run_github_scraper(self.token, "python", 2)

        mock_print.assert_has_calls([
            call('Found 2 users related to tag "python"'),
            call('Saved data for user bob to bob.json'),
            call('Saved data for user charlotte to charlotte.json'),
            call('----- DONE -----')
        ])


if __name__ == '__main__':
    unittest.main()
