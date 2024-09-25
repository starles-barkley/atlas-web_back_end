#!/usr/bin/env python3
'''Test module for client'''
import unittest
from unittest.mock import patch
from parameterized import parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


@parameterized_class([
    {"org_payload": org_payload, "repos_payload": repos_payload,
     "expected_repos": expected_repos, "apache2_repos": apache2_repos}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for GithubOrgClient.public_repos method."""

    @classmethod
    def setUpClass(cls):
        """Set up class to mock external requests."""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def get_json(url):
            if url == "https://api.github.com/orgs/google":
                return cls.org_payload
            elif url == "https://api.github.com/orgs/google/repos":
                return cls.repos_payload
            return None

        cls.mock_get.return_value.json.side_effect = get_json

    @classmethod
    def tearDownClass(cls):
        """Tear down class to stop patching."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test GithubOrgClient.public_repos integration with repos_payload."""
        client = GithubOrgClient("google")
        repos = client.public_repos()

        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """Test GithubOrgClient.public_repos with a license filter (apache-2.0)."""
        client = GithubOrgClient("google")
        repos = client.public_repos(license_key="apache-2.0")

        self.assertEqual(repos, self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
