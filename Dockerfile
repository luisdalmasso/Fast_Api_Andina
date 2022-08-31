FROM python:3.10

COPY . /app
WORKDIR /app


COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /Fast_Api_Andina/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
