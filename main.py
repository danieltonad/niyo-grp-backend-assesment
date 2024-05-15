from fastapi import FastAPI


app = FastAPI(title="Niyo Group Backend Assessment")

@app.get('/')
async def roor():
    return "__init__"