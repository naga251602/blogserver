"""
This is the main file consists of main server-code
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from models.reqResModels import LoginInModel
from routes.userRoutes import user_router
from routes.postRoutes import post_router
from services.authentication import auth_router
import uvicorn
from utils.htmlWelcome import htmlContent


# creating a api instance
app = FastAPI()


@app.get("/")
def home():
    """
    This is just a home page consists of links to docs
    """
    return HTMLResponse(content=htmlContent, status_code=200)


# including all other routes of the app
app.include_router(user_router)  # adds user endpoints
app.include_router(auth_router)  # adds the authentication endpoints
app.include_router(post_router)  # adds the posts endpoints post

if __name__ == "__main__":
    uvicorn.run(app)
