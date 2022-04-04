# unserial-django-demo

- https://docs.python.org/3/library/pickle.html
- https://docs.djangoproject.com/en/4.0/topics/http/sessions/



## code points 

- venv/lib/python3.8/site-packages/django/contrib/sessions/backends/signed_cookies.py:67
- venv/lib/python3.8/site-packages/django/contrib/sessions/backends/base.py:180
- django.core.serializers.base.PickleSerializer.loads : sink
- django.core.signing.Signer.unsign_object : signature


- django.contrib.sessions.backends.base.SessionBase._get_session : get session
- django.contrib.sessions.backends.signed_cookies.SessionStore: session store
  - appel de signing.loads avec le serializer
  - django.core.signing.Signer.unsign_object
    - c'est ici qu'on opère le déchiffrement + decompression si besoin + deserialisation
    - ligne 219 : on va vers la vérification de signature
    - django.core.signing.TimestampSigner.unsign
      - django.core.signing.Signer.unsign
        - Ici on vérifie la signature
          - split des paries de la signature
          - [.]<PAYLOAD>:<TIME>:SIG
          - django.core.signing.Signer.signature: on signe la valeur en hmac pour comparer C'est ce moceau de code qui nous permet de reproduire la signature avec la clé
          - Et le sel ? Il pourrait être généré mais ce n'est pas le cas, il est fixe et prédictible
      - Si la signature est ok
    - on extrait le timestamp en base62
    - On vérifie le timing
  - on récupère le base64 hors signaure
  - On le décompresse si il y a un '.' au début
  - On deserialize \o/

## payload

[.]<PAYLOAD>:<TIME>:SIG

- . if compressed
- pickle base64 with zlib if compressed
- b62_encode(int(time.time()))
- base64_hmac( self.salt + "signer", value, self.key, algorithm=self.algorithm)
  - salt = 'django.contrib.sessions.backends.signed_cookies'
  - algorithm = 'sha256'

## template

credit : https://www.free-css.com/free-css-templates/page276/transportz