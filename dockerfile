FROM python:3.11 

ENV PYTHONUNBUFFERED=1

WORKDIR /EXECL_FILE_UPLOAD

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . /EXECL_FILE_UPLOAD

EXPOSE 8000

CMD ["python","manage.py", "runserver", "0.0.0.0:8000"]

