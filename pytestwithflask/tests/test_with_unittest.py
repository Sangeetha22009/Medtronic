import unittest


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Perform setup tasks for the entire test class
        print("Setting up the test class")

    def setUp(self):
        # Perform setup tasks before each test method
        print("Setting up the test")

    def test_example(self):
        # Test case
        print("Running the test2")

    def test_example2(self):
        # Test case
        print("Running the test")

    def tearDown(self):
        # Perform teardown tasks after each test method
        print("Tearing down the test")

    @classmethod
    def tearDownClass(cls):
        # Perform teardown tasks for the entire test class
        print("Tearing down the test class")
