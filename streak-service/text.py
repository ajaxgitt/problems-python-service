

import sys
import io

def run_code_in_sandbox(code: str, result_variable='output'):
    sandbox = {}
    output = io.StringIO()
    sys.stdout = output

    try:
        exec(code, {"__builtins__": None}, sandbox)
        result = sandbox.get(result_variable, "No result found")  
        return {"result": output.getvalue(), "sandbox": sandbox, "return": result}
    except Exception as e:
        raise RuntimeError(f"Error al ejecutar el código: {e}")
    finally:
        sys.stdout = sys.__stdout__  


code = """
def sum(a, b):
    return a + b
output = sum(5, 9)  # El usuario usa 'output'
"""


print(run_code_in_sandbox(code=code))



