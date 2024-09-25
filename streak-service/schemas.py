
from pydantic import BaseModel
from typing import List
from datetime import datetime


        
class History(BaseModel):
    usuario_id : int
    fecha_completado : datetime
    estado : bool
    calificacion : int
    
    class Config:
        orm_mode = True

class CreateExercise(BaseModel):
    nombre : str
    problema :str
    pista : str
    solucion : str
    
    class Config:
        orm_mode = True
        

    
    