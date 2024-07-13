from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import logging
from datetime import datetime
from src.services.email import send_mail_task

app = FastAPI()

# Configure logging
# logging.basicConfig(filename='/var/log/messaging_system.log', level=logging.INFO)

# Pydantic models
class SendMailParams(BaseModel):
    sendmail: str

@app.get("/")
def root():
    return {"message": "Messaging system is running"}

@app.post("/sendmail")
def send_mail(params: SendMailParams):
    send_mail_task.delay(params.sendmail)
    return {"message": f"Email task for {params.sendmail} has been queued"}

@app.get("/talktome")
def talk_to_me(talktome: bool = Query(False)):
    if talktome:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logging.info(f"Current time logged: {current_time}")
        return {"message": f"Current time {current_time} logged successfully"}
    else:
        raise HTTPException(status_code=400, detail="Invalid parameter")
