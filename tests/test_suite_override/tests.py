import unittest

from django.apps import app_cache
from django.test.utils import IgnoreAllDeprecationWarningsMixin


def suite():
    testSuite = unittest.TestSuite()
    testSuite.addTest(SuiteOverrideTest('test_suite_override'))
    return testSuite


class SuiteOverrideTest(IgnoreAllDeprecationWarningsMixin, unittest.TestCase):

    def test_suite_override(self):
        """
        Validate that you can define a custom suite when running tests with
        ``django.test.simple.DjangoTestSuiteRunner`` (which builds up a test
        suite using ``build_suite``).
        """

        from django.test.simple import build_suite
        app_config = app_cache.get_app_config("test_suite_override")
        suite = build_suite(app_config)
        self.assertEqual(suite.countTestCases(), 1)


class SampleTests(unittest.TestCase):
    """These tests should not be discovered, due to the custom suite."""
    def test_one(self):
        pass

    def test_two(self):
        pass

    def test_three(self):
        pass
