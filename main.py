from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router as api_router
#from scripts.get_events import get_all_events
#from scripts.count_points import update_total_points
#from deta import App
import datetime

app=FastAPI()
origin= [
    'http://localhost',
    'http://localhost:4200'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods={"*"},
    allow_headers={"*"}
)

app.include_router(api_router)

""" @app.lib.cron()
def cron_job_all_events(event = None):
    get_all_events()

    if datetime.datetime.now().hour >= 16 :
        update_total_points()

    return "Done" """