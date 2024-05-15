from fastapi import FastAPI
from api.users import users
from api.tasks import tasks


app = FastAPI(
    title="Niyo Group Backend Assessment",
    # redoc_url=None,
    # docs_url=None
    )

app.include_router(router=users)
app.include_router(router=tasks)