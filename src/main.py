"""Main file for start app."""
import uvicorn
from fastapi import FastAPI

from src.forms.router import router as router_form

# Create a FastAPI application instance
app = FastAPI()

# Include the router for forms
app.include_router(router_form)

# Run the FastAPI application using uvicorn server
if __name__ == '__main__':
    uvicorn.run(app='main:app', host='127.0.0.1', port=8000, reload=True)
