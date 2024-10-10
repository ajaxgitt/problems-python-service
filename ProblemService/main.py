from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from .router import streak


description = """
#Este servicio es para obtener todos los problemas o retos que estan fuera de los modulos de aprendisaje
"""

app = FastAPI(

    title="Servicio Problemas",
    description=description,
    summary="Deadpool's favorite app. Nuff said.",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Deadpoolio the Amazing",
        "url": "http://x-force.example.com/contact/",
        "email": "dp@x-force.example.com",
    },
    license_info={
        "name": "Sherlock 1.0",
        "url": "https://react-sherlock.vercel.app/",
    },
)
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


