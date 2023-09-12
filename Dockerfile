# 
FROM python:3.9

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt
COPY ./teste_api.pkl /code/teste_api.pkl
# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app.py /code/app.py

# 
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]