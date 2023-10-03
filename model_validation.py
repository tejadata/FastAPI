from pydantic import BaseModel,field_validator,EmailStr
from typing import List,Optional
import json
class address(BaseModel):
    primary: str
    secondary: str

    @field_validator('primary')
    def primary(cls,value):
        if len(value)>30:
            raise ValueError("Address should not be more than 20 charecters in lenght")
        return value 
    
    @field_validator('secondary')
    def secondary(cls,value):
        if len(value)>30:
            raise ValueError("Address should not be more than 20 charecters in lenght")
        return value 

class items(BaseModel):
    item_name: str
    sku: str
    quantity: int
    price: float
    deliverd: bool

class Customer(BaseModel):
    name: str
    phone: str
    email: EmailStr
    address: address
    Items: List[items]

class cust_id(BaseModel):
    name: str

"""with open('customer.json') as cust:
    data = json.loads(cust.read())
    customer = Customer(**data)

print(customer)"""