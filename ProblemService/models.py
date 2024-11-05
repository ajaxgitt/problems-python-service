from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, JSON, Text, TIMESTAMP
from .database import Base, engine
from sqlalchemy import func
from sqlalchemy.orm import relationship


class SolvedExercises(Base):
    __tablename__ = 'solvedExercises'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    exercise_id = Column(Integer, ForeignKey("exercise.id"), nullable=False)
    usuario_id = Column(Integer, nullable=False)  
    fecha_completado = Column(TIMESTAMP, server_default=func.now(), nullable=True) 
    resultado = Column(Boolean, default=False)

    exercise = relationship("Exercise", back_populates="historial")


class TestCase(Base):
    __tablename__ = "test_case"

    id = Column(Integer, primary_key=True)
    entrada = Column(String(255)) 
    salida_esperada = Column(String(255))
    exercise_id = Column(Integer, ForeignKey('exercise.id'))

    exercise = relationship("Exercise", back_populates="casos_de_prueba")


    

class Exercise(Base):
    __tablename__ = "exercise"

    id = Column(Integer, primary_key=True)
    nombre_funcion = Column(String(255)) 
    nombre = Column(String(255), index=True)
    problema = Column(Text)
    pista = Column(String(255), index=True)
    dificultad = Column(Integer, nullable=False)  
    
    
    casos_de_prueba = relationship("TestCase", back_populates="exercise", cascade="all, delete-orphan")
    historial = relationship("SolvedExercises", back_populates="exercise")





class Exercise_Senior(Base):
    __tablename__ = "exercise_Senior"
    
    id = Column(Integer, primary_key=True)
    nombre_funcion = Column(String(255)) 
    nombre = Column(String(255), index=True)
    problema = Column(Text)
    dificultad = Column(Integer, nullable=False)  
    
    casos_de_prueba = relationship("TestCase_Senior", back_populates="exercise_Senior", cascade="all, delete-orphan")
    historial = relationship("SolvedExercises_Senior", back_populates="exercise_Senior")

class TestCase_Senior(Base):
    __tablename__ = "testCase_Senior"

    id = Column(Integer, primary_key=True)
    entrada = Column(String(255)) 
    salida_esperada = Column(String(255))
    exercise_id = Column(Integer, ForeignKey('exercise_Senior.id'))  

    exercise_Senior = relationship("Exercise_Senior", back_populates="casos_de_prueba")
    

class SolvedExercises_Senior(Base):
    __tablename__ = 'solvedExercises_Senior'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    exercise_id = Column(Integer, ForeignKey("exercise_Senior.id"), nullable=False)  
    usuario_id = Column(Integer, nullable=False)  
    fecha_completado = Column(TIMESTAMP, server_default=func.now(), nullable=True) 
    resultado = Column(Boolean, default=False)

    exercise_Senior = relationship("Exercise_Senior", back_populates="historial")
    
    
    
    

Base.metadata.create_all(bind=engine)