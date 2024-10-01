from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from .router import streak



app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")



origins = [
    "http://127.0.0.1:8000",
    "http://localhost:5173",
    "https://react-sherlock-git-main-yecids-projects.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

app.include_router(streak)


