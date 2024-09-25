from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, JSON, Text, TIMESTAMP
from .database import Base, engine
from sqlalchemy import func
from sqlalchemy.orm import relationship


class HistorialExercise(Base):
    __tablename__ = 'historialExercise'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, nullable=False)  
    exercise_id = Column(Integer, ForeignKey("exercise.id"), nullable=False)
    fecha_completado = Column(TIMESTAMP, server_default=func.now(), nullable=True) 
    estado = Column(Boolean, default=False)
    calificacion = Column(Integer, nullable=False) # es obligatorio

    exercise = relationship("Exercise", back_populates="historial")


class Exercise(Base):
    __tablename__ = "exercise"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(255), index=True)
    problema = Column(Text)
    pista = Column(String(255), index=True)
    descripcion_code = Column(Text)
    solucion = Column(String(255), index=True)
    
    historial = relationship("HistorialExercise", back_populates="exercise")
    
    

Base.metadata.create_all(bind=engine)