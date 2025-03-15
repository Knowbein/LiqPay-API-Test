import base64
import json
import hashlib

class LiqPay:
    def __init__(self, public_key, private_key):
        self.public_key = public_key
        self.private_key = private_key

    def cnb_form(self, params):
        params['public_key'] = self.public_key
        data = base64.b64encode(json.dumps(params).encode()).decode()
        signature = self._str_to_sign(self.private_key + data + self.private_key)
        signature = base64.b64encode(hashlib.sha1(signature.encode()).digest()).decode()
        return data, signature

    def _str_to_sign(self, str_data):
        return str_data
