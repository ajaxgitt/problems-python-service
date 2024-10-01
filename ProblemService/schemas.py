
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
        

class TestCase(BaseModel):
    entrada: str
    salida_esperada: str

class CreateExercise(BaseModel):
    nombre: str
    problema: str
    pista: str
    dificultad: int
    casos_de_prueba: List[TestCase]  # Cambia aquí a casos_de_prueba

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
        

    
    