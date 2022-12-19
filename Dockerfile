FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
EXPOSE 8000
COPY . /code
RUN pip install -r requirements.txt
RUN ls -l
ENTRYPOINT ["python", "manage.py", "runserver 0.0.0.0:8000"]

