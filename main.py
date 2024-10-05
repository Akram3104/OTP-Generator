# fastapi_app.py (FastAPI server)

from fastapi import FastAPI
from pydantic import BaseModel
import time

app = FastAPI()

a = 1664525   
c = 1013904223  
m = 2**32    
seed = 12345
class OTPRequest(BaseModel):
    length: int

def linear_congruence(length):
    otp = ""
    global seed
    x = seed
    for _ in range(length):
        x = (a * x + c) % m
        otp += str(x % 10)  
    seed = x
    return otp

@app.post("/generate-otp/")
def generate_otp(request: OTPRequest):
    # seed = int(time.time())  # Using current time as seed
    # seed = 12345
    
    otp = linear_congruence(request.length)
    return {"otp": otp}
