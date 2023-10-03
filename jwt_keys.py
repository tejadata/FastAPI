import jwt
import datetime
import cryptography.fernet

# Your secret key to encode the JWT token. This should be kept private.
SECRET_KEY = "/Users/bhanuteja/jwt/my_key"
SECRET_KEY = "/Users/bhanuteja/jwt/private_key.pem"
with open(SECRET_KEY, 'r') as f:
    private_key = f.read()

payload = {
    "user_id": 42,
    "username": "alice",
    "role": "admin",
    # "exp" sets the expiration time for the token. Here, it expires after 1 hour.
    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=100)
}

# Generate the JWT token
token = jwt.encode(payload, private_key, algorithm="RS256")
print("------------------------")
print(f"Generated JWT token: {token}")


with open('/Users/bhanuteja/jwt/public_key.pem', 'r') as f:
    public_key = f.read()
try:
    decoded_data = jwt.decode(jwt=token,
                              key=public_key,
                              algorithms=["RS256"])

    print(decoded_data)
except jwt.ExpiredSignatureError:
    print("Token has expired")
except jwt.DecodeError:
    print("Token is invalid")
