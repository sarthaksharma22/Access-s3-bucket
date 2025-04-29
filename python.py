from datetime import datetime, timedelta
from cryptography.hazmat.primitives import serialization
from cloudfront_signer import CloudFrontSigner

def rsa_signer(message):
    with open("private_key.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(key_file.read(), password=None)
    return private_key.sign(message)

key_id = "<Your-Key-ID>"
url = "https://<your-cloudfront-domain-name>/"

cloudfront_signer = CloudFrontSigner(key_id, rsa_signer)

# Generate cookies that expire in 1 hour
cookies = cloudfront_signer.get_signed_cookie(
    url,
    date_less_than=datetime.utcnow() + timedelta(hours=1)
)

print(cookies)
