from fastapi import FastAPI, Request
from datetime import datetime, timedelta, timezone

app = FastAPI()

@app.get("/")
async def root(request: Request):
    client_ip = request.client.host
    
    # 1. Create a timezone object for IST (UTC +5:30)
    IST = timezone(timedelta(hours=5, minutes=30))
    
    # 2. Get the current time in IST and format it
    # %d = day, %m = month, %Y = 4-digit year, %H:%M:%S = time
    ist_now = datetime.now(IST).strftime("%d-%m-%Y %H:%M:%S")
    
    return {
        "timestamp": ist_now,
        "ip": client_ip
    }