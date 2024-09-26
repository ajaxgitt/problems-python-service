
from pydantic import BaseModel
from typing import List
from datetime import datetime



class CodeSubmission(BaseModel):
    user_id: int
    codigo: str

        
class History(BaseModel):
    id :int
    usuario_id : int
    exercise_id : int
    fecha_completado : datetime
    resultado : bool
    
    class Config:
        orm_mode = True
        
class HistoryExercise(BaseModel):
    usuario_id : int
    exercise_id : int
    
    class Config:
        orm_mode = True
        
        
class CreateHistory(BaseModel):
    exercise_id : int
    
    class Config:
        orm_mode = True
        


class CreateExercise(BaseModel):
    nombre : str
    problema :str
    pista : str
    dificultad : int
    solucion : str
    
    class Config:
        orm_mode = True
        
class ExerciseResponse(BaseModel):
    id : int
    nombre : str
    problema :str
    dificultad : int
    pista : str
    
    class Config:
        orm_mode = True
        

    
    