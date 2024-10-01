FROM python:3.12.4

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./ProblemService /code/ProblemService

CMD ["uvicorn", "ProblemService.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
