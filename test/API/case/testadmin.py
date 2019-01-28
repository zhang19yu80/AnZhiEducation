from config import config
import unittest, time, requests

class TestAdmin(unittest.TestCase):
    def __init__(self):
        self.host_url = config.Config().get('URL')
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_login(self):
        






