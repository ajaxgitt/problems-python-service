
from pydantic import BaseModel
from typing import List ,Optional
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
        
        
        

class TestCaseShema(BaseModel):
    entrada: str
    salida_esperada: str




class CreateExercise(BaseModel):
    nombre: str
    nombre_funcion:str
    problema: str
    pista: str
    dificultad: int
    exp:int
    casos_de_prueba: List[TestCaseShema]  

    class Config:
        orm_mode = True
        


        
class CreateExercise_Senior(BaseModel):
    nombre: str
    nombre_funcion:str
    problema: str
    dificultad: int
    casos_de_prueba: List[TestCaseShema]  

    class Config:
        orm_mode = True
        
        
        

        
class ExerciseResponse(BaseModel):
    id : int
    nombre_funcion:str
    nombre : str
    problema :str
    dificultad : int
    casos_de_prueba : List[TestCaseShema]
    pista : str
    exp:int
    
    
    class Config:
        orm_mode = True
        
class ExerciseResponse_Senior(BaseModel):
    id : int
    nombre_funcion:str
    nombre : str
    problema :str
    dificultad : int
    casos_de_prueba : List[TestCaseShema]
    
    class Config:
        orm_mode = True
        

     
class Argumentos(BaseModel):
    id : int
    nombre : str
    nombre_funcion:str
    problema :str
    casos_prueba : List[TestCaseShema]
    
    class Config:
        orm_mode = True
        
        

        
class Top(BaseModel):
    usuario_id : int
        

        
    
    
class Toop(BaseModel):
    usuario_id : int
    puntuacion : int