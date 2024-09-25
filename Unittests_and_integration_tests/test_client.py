#!/usr/bin/env python3
'''Test module for client'''
import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Unit test for the GithubOrgClient class."""

    @patch('client.get_json')
    def test_org(self, mock_get_json):
        """Test that GithubOrgClient.org returns the expected value."""
        mock_get_json.return_value = {"login": "google"}
        client = GithubOrgClient("google")
        result = client.org
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/google"
        )
        self.assertEqual(result, {"login": "google"})

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test that GithubOrgClient._public_repos_url returns the expected URL."""
        mock_org.return_value = {
            "repos_url": "https://api.github.com/orgs/google/repos"
        }

        client = GithubOrgClient("google")

        result = client._public_repos_url

        self.assertEqual(result, "https://api.github.com/orgs/google/repos")

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test that GithubOrgClient.public_repos returns the expected repos."""
        mock_public_repos_url.return_value = "https://api.github.com/orgs/google/repos"
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]

        client = GithubOrgClient("google")

        result = client.public_repos()

        self.assertEqual(result, ["repo1", "repo2", "repo3"])

        mock_public_repos_url.assert_called_once()

        mock_get_json.assert_called_once_with("https://api.github.com/orgs/google/repos")


if __name__ == '__main__':
    unittest.main()
