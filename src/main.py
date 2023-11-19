import uvicorn
from fastapi import FastAPI

from src.forms.routers import router as router_form

app = FastAPI()

app.include_router(router_form)

if __name__ == '__main__':
    uvicorn.run(app='main:app', host='127.0.0.1', port=8000, reload=True)
