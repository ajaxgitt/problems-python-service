from fastapi import APIRouter
from . database import SessionLocal
from .schemas import *
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends
from .models import Exercise , SolvedExercises , TestCase
from .services import *

import httpx


streak = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
        





        
@streak.post('/api/create/', response_model=CreateExercise ,tags=['crear'])
def create_exercice(exercise: CreateExercise, db: Session = Depends(get_db)):
    """Función para crear un nuevo ejercicio"""
    # Crear el nuevo ejercicio
    new_exercise = Exercise(
        nombre=exercise.nombre,
        nombre_funcion = exercise.nombre_funcion,
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



@streak.post('/api/createhistory/{token}',tags=['crear'])
def create_history(token:str, history: CreateHistory ,db:Session=Depends(get_db)):
    """funcion para crear un historial para el user y marcar todos los ejercicos resuletos """
    
    id_user = verify_token(token=token)
    id_token = int(id_user['sub'])
    
    new_fistory = SolvedExercises(
         usuario_id = id_token,
        exercise_id = history.exercise_id,
        resultado = True
        
    )
    db.add(new_fistory)
    db.commit()
    db.refresh(new_fistory)
    
    return new_fistory




@streak.get('/api/get_exercice', response_model=List[ExerciseResponse],tags=['obtener'])
def get_exercise(db : Session = Depends(get_db)):
    """funcion para llamar a todos los ejercicios"""
    ejercicios = db.query(Exercise).all()
    return ejercicios






@streak.get('/api/exercice/{id}', response_model=ExerciseResponse,tags=['obtener'])
def get_exercice_id(id:int,db:Session= Depends(get_db)):
    """funcion para llamar a un ejercicio por su id"""
    
    ejercicio_db = db.query(Exercise).filter(Exercise.id == id).first()
    
    if ejercicio_db is None:
        raise HTTPException(status_code=404 , detail="ejercicio no encontrado en la base de datos")
    response = ExerciseResponse(
        id=ejercicio_db.id,
        nombre_funcion=ejercicio_db.nombre_funcion,
        nombre=ejercicio_db.nombre,
        problema=ejercicio_db.problema,
        dificultad=ejercicio_db.dificultad,
        casos_de_prueba=[TestCaseShema(entrada=caso.entrada, salida_esperada=caso.salida_esperada) for caso in ejercicio_db.casos_de_prueba],
        pista=ejercicio_db.pista
    )

    
    return response
    
    
    
    
    

@streak.post('/api/exercice/{id}',tags=['crear'])
def get_exercice_id(id:int,db:Session= Depends(get_db)):
    """funcion para llamar a un ejercicio por su id
    y devolver los argumentos para corrrer el interprete"""
    
    ejercicio_db = db.query(Exercise).filter(Exercise.id == id).first()
    if ejercicio_db is None:
        raise HTTPException(status_code=404 , detail="ejercicio no encontrado en la base de datos")
    
    args = {
        'nombre_funcion':ejercicio_db.nombre_funcion,
        'codigo':'aqui se pondria el codigo del user',
        'problema': ejercicio_db.problema,
        'casos_prueba': ejercicio_db.casos_de_prueba
    }
    return args
    



@streak.get('/api/history/{token}', response_model=List[History] ,tags=['obtener'])
def get_history(token:str, db:Session=Depends(get_db)):
    """funcion para consultar la lista de ejercicios resuletos por el usuario"""
    id_user = verify_token(token=token)
    id_token = int(id_user['sub'])
    
    print(f"el id del user es: {id_token}")
    
    history = db.query(SolvedExercises).filter(SolvedExercises.usuario_id == id_token).all()
    if history is None:
        raise HTTPException(status_code=404 , detail="user is not found")
    
    return history





@streak.get('/api/top_users/{id}', tags=['optener_Top'])
def get_top_id(id:int,db:Session=Depends(get_db)):
    top = db.query(SolvedExercises).filter(SolvedExercises.usuario_id == id).all()
    return top


@streak.get('/api/top_users', response_model=List[Toop],tags=['optener_Top'])
def get_top( db:Session=Depends(get_db)):
    try:
        results = db.query(SolvedExercises).all()
        top_users = [
            Top(
                usuario_id = exercise.usuario_id,
            )for exercise in results
        ]
        
        users = []
        for i in top_users:
            for j in i:
                users.append(j[1])
        users_ordenados = sorted(users)     
        contendientes = sorted(list(set(users)))
        
        cap = {}
        
        for i in range(len(contendientes)):
            suma = len(list(filter(lambda x : x == contendientes[i], users_ordenados)))
            cap[contendientes[i]] = suma
            
        top = dict(sorted(cap.items(), key=lambda x : x[1], reverse=True))
        
        res = [
            Toop(
                usuario_id=k,
                puntuacion=v,
            ) for k ,v in top.items()
        ]
            
        return res
    
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


