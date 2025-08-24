# test_fuzzysearch.py
"""
Tests for FuzzySearch module.
"""

import unittest
from fuzzysearch import FuzzySearch

class TestFuzzySearch(unittest.TestCase):
    """Test cases for FuzzySearch class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FuzzySearch()
        self.assertIsInstance(instance, FuzzySearch)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FuzzySearch()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
