from fastapi import FastAPI
from api.users import users
from api.tasks import tasks
from settings import settings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title=settings.APP_NAME,
    # redoc_url=None,
    # docs_url=None
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST", "GET", "PATCH", "DELETE"],
    allow_headers=["*"],
)

app.include_router(router=users, prefix=settings.API_VERSION)
app.include_router(router=tasks, prefix=settings.API_VERSION)