import base64
import urllib
import urllib.request


class AuthOpener(object):
    def __init__(self, cred_path):
        self.cred_path = cred_path
        self.auth = self._get_auth()
        self.opener = None

    def _get_auth(self):
        cred_path = self.cred_path
        with open(cred_path, 'r') as f:  # transform request form
            cred = f.read()
            cred = cred.strip()
            cred = cred.encode('ascii')
            cred = base64.b64encode(cred)
            cred = cred.decode('utf-8')
            return cred

    def get_opener(self):
        if self.opener is not None:
            return self.opener
        self.opener = urllib.request.build_opener()
        self.opener.addheaders = [('Authorization', 'Basic ' + self.auth)]
        return self.opener
