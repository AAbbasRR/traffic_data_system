FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY . /code/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

RUN python -m unittest test -v

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]