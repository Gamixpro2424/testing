from fastapi import FastAPI
import uvicorn
import string
import random 
app = FastAPI()

@app.get('/random-gen')
async def generate_random_integer():
    a = [1,2,3,4,5,6,7,8,9,0]
    b = random.sample(a,5)
    result_string = "".join(map(str, b))
    return int(result_string)

