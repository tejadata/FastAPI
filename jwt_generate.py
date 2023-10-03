import jwt
import datetime

payload = {
    "user_id": 42,
    "username": "alice",
    "role": "admin",
    # "exp" sets the expiration time for the token. Here, it expires after 1 hour.
    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=2000)
}

# Generate the JWT token
token = jwt.encode(payload, "hasodfhsajkfskfajn", algorithm="HS256")
print("------------------------")
print(f"Generated JWT token: {token}")


print(jwt.decode(token, "hasodfhsajkfskfajn", algorithms=["HS256"]))
