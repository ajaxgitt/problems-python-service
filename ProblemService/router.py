from fastapi import APIRouter
from . database import SessionLocal
from .schemas import *
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends
from .models import Exercise , SolvedExercises
from .services import *
from pydantic import BaseModel
import ast


streak = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@streak.post('/api/create/', response_model=CreateExercise)
def create_exercice(exercise: CreateExercise, db: Session = Depends(get_db)):
    """Función para crear un nuevo ejercicio"""
    # Crear el nuevo ejercicio
    new_exercise = Exercise(
        nombre=exercise.nombre,
        problema=exercise.problema,
        pista=exercise.pista,
        dificultad=exercise.dificultad
    )
    
    # Agregar los casos de prueba
    for case in exercise.casos_de_prueba:
        test_case = TestCase(
            entrada=case.entrada,
            salida_esperada=case.salida_esperada,
            exercise=new_exercise  # Establecer la relación
        )
        new_exercise.casos_de_prueba.append(test_case)

    db.add(new_exercise)
    db.commit()
    db.refresh(new_exercise)
    
    return new_exercise




@streak.get('/api/exercice/', response_model= List[CreateExercise])
def get_exercice( db : Session = Depends(get_db)):
    """funcion para llamar a todos los ejercicios"""
    ejercicios = db.query(Exercise).all()
    return ejercicios


@streak.post('/api/history/{id}')
def create_history(id:int, history: CreateHistory ,db:Session=Depends(get_db)):
    new_fistory = SolvedExercises(
         usuario_id = id,
        exercise_id = history.exercise_id,
    )
    db.add(new_fistory)
    db.commit()
    db.refresh(new_fistory)
    
    return new_fistory


@streak.get('/api/exercice/{id}', response_model=ExerciseResponse)
def get_exercice_id(id:int,db:Session= Depends(get_db)):
    """funcion para llamar a un ejercicio por su id"""
    
    ejercicio_db = db.query(Exercise).filter(Exercise.id == id).first()
    if ejercicio_db is None:
        raise HTTPException(status_code=404 , detail="ejercicio no encontrado en la base de datos")
    return ejercicio_db
    

@streak.get('/api/history/{token}', response_model=List[History])
def get_history(token:str, db:Session=Depends(get_db)):
    """funcion para consultar la lista de ejercicios resuletos por el usuario"""
    id_user = verify_token(token=token)
    id_token = int(id_user['sub'])
    
    print(f"el id del user es: {id_token}")
    
    history = db.query(SolvedExercises).filter(SolvedExercises.usuario_id == id_token).all()
    if history is None:
        raise HTTPException(status_code=404 , detail="user is not found")
    
    return history



        
        

# @streak.post("/api/execute_code/")
# async def execute_code(code_submission: CodeSubmission):
#     try:
#         # Validar la sintaxis del código
#         ast.parse(code_submission.codigo)  # Lanzará un error si hay un problema de sintaxis

#         # Ejecutar el código en un sandbox
#         result = run_code_in_sandbox(code_submission.codigo)
#         return result

#     except SyntaxError as e:
#         raise HTTPException(status_code=400, detail="Error de sintaxis en el código.")
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="Error al ejecutar el código.")









