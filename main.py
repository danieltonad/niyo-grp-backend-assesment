from fastapi import FastAPI
from api.users import users
from api.tasks import tasks
from settings import settings


app = FastAPI(
    title=settings.APP_NAME,
    # redoc_url=None,
    # docs_url=None
    )

app.include_router(router=users, prefix=settings.API_VERSION)
app.include_router(router=tasks, prefix=settings.API_VERSION)