#!/usr/bin/env python3
'''Util Testing Module'''
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Unit test for the access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map returns the expected value."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    def test_access_nested_map_exception(self, nest, path):
        """Test access_nested_map raises KeyError with correct message."""
        with self.assertRaises(KeyError):
            utils.access_nested_map(nest, path)


if __name__ == '__main__':
    unittest.main()
