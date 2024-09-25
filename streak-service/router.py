from fastapi import APIRouter
from . database import SessionLocal
from .schemas import *
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends
from .models import Exercise , HistorialExercise


streak = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        


@streak.post('/api/create/', response_model= CreateExercise)
def create_exercice(exercise : CreateExercise, db : Session = Depends(get_db)):
    new_exercise = Exercise(
        nombre = exercise.nombre,
        problema = exercise.problema,
        pista = exercise.pista,
        solucion = exercise.solucion)
    
    db.add(new_exercise)
    db.commit()
    db.refresh(new_exercise)
    
    return new_exercise

@streak.get('/api/exercice/', response_model= List[CreateExercise])
def get_exercice( db : Session = Depends(get_db)):
    ejercicios = db.query(Exercise).all()
    
    return ejercicios


