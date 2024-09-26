from decouple import config
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from fastapi import HTTPException, Depends
import sys
import io

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "token")


def verify_token(token:str =Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, config('SECRET_KEY'), algorithms=[config('ALGORITHM')])
        id_user: str = payload.get("sub")
        if id_user is None:
            raise HTTPException(status_code=403, detail="token is invalid or expired")
        return payload 
    except JWTError:
        raise HTTPException(status_code=403, detail="token is invalid or expired")


import io
import sys

def run_code_in_sandbox(code: str):
    # Limitar el contexto de ejecución
    sandbox = {}
    
    # Redirigir la salida estándar para capturar prints
    output = io.StringIO()
    sys.stdout = output

    try:
        # Ejecutar el código en un entorno controlado
        exec(code, {"__builtins__": None}, sandbox)
        result = output.getvalue()  # Capturar cualquier salida
        return {"result": result, "sandbox": sandbox, "error": False}
    except Exception as e:
        # Retornar un mensaje de error estructurado
        return {"result": str(e), "error": True}
    finally:
        sys.stdout = sys.__stdout__  # Restaurar la salida estándar
