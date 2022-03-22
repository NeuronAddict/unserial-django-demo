# unserial-django-demo

- https://docs.python.org/3/library/pickle.html
- https://github.com/gintas/django-picklefield

## payload

[.]<PAYLOAD>:<TIME>:SIG

- . if compressed
- pickle base64 with zlib if compressed
- b62_encode(int(time.time()))
- base64_hmac( self.salt + "signer", value, self.key, algorithm=self.algorithm)
  - salt = 'django.contrib.sessions.backends.signed_cookies'
  - algorithm = 'sha256'

