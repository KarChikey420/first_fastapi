import secrets
import base64

key=base64.urlsafe_b64encode(secrets.token_bytes(32))
print(key.decode())