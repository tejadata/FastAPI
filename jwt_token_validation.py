from fastapi import Request, HTTPException
import jwt


with open('/Users/bhanuteja/jwt/public_key.pem', 'r') as f:
    public_key = f.read()
resources = ['/get', '/role', '/customer']


async def token(req: Request):
    resource = str(req.url.path)
    print("In JWT validation")
    if req.headers.get('authorization'):
        try:
            # print(req.headers.get('authorization')[7:])
            decoded_data = jwt.decode(jwt=req.headers.get('authorization')[7:],
                                      key=public_key,
                                      algorithms=["RS256"])
            print(decoded_data)
            if decoded_data['role'] != 'admin' or resource not in resources:
                print("Not satisfied")
                raise HTTPException(
                    status_code=401, detail="You dont have access to this resource")

        except jwt.ExpiredSignatureError as e:
            raise HTTPException(status_code=401, detail=str(e))
        except jwt.DecodeError as e:
            raise HTTPException(status_code=401, detail=str(e))
        except jwt.exceptions.InvalidAlgorithmError as e:
            raise HTTPException(status_code=401, detail=str(e))
    else:
        raise HTTPException(status_code=404, detail='User not found')
    print("123")
    return 1
