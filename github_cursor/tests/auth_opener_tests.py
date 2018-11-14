import unittest
import os
import urllib.request

from github_cursor.modules.auth_opener import AuthOpener

FILENAME = 'test_file'


class AuthOpenerTestCase(unittest.TestCase):
    def setUp(self):
        with open(FILENAME, 'w') as f:
            f.write('IDinHere:PASSWDinHere')

    def tearDown(self):
        if os.path.exists(FILENAME):
            os.remove(FILENAME)

    def test___init__(self):
        opener = AuthOpener(FILENAME)
        self.assertEqual(FILENAME, opener.cred_path)
        self.assertEqual(None, opener.opener)

    def test__get_auth(self):
        opener = AuthOpener(FILENAME)
        self.assertEqual('SURpbkhlcmU6UEFTU1dEaW5IZXJl', opener._get_auth())

    def test_get_opener(self):
        opener = AuthOpener(FILENAME)
        self.assertEqual(urllib.request.OpenerDirector, type(opener.get_opener()))
