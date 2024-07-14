from fastapi import FastAPI, Query
from datetime import datetime
import aiofiles
import os
from src.services.email import send_mail_task

app = FastAPI()

@app.get("/")
async def root(sendmail: str = Query(None), talktome: bool = Query(False)):
    if sendmail:
        send_mail_task.delay(sendmail)
        return {"message": f"Email will be sent to {sendmail}"}

    if talktome:
        log_message = f"{datetime.now()}\n"
        async with aiofiles.open("/var/log/messaging_system.log", mode="a") as log_file:
            await log_file.write(log_message)
        return {"message": "Current time logged"}

    return {"message": "Invalid request"}