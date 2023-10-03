from fastapi import FastAPI, Depends
import json
from pydantic import ValidationError
from model_validation import Customer, cust_id
from jwt_token_validation import token

app = FastAPI()


@app.post("/customer", response_model=Customer)
async def read_item(req: cust_id, reqs: str = Depends(token)):
    print("In the rest -----------", req)
    try:
        with open('customer.json') as data:
            data = json.loads(data.read())
        return Customer(**data)
    except ValidationError as error:
        errors = error.errors()
        print(errors)
        res = {"number of columns": len(errors), "columns name": [(
            columns['loc'], columns['msg']) for columns in errors]}
        return res
    except Exception as err:
        print(err)
        return str(err)
