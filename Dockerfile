FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requeriments.txt /code/
COPY . /code/
RUN pip3 install -r requeriments.txt && echo "finished"
RUN python3 manage.py collectstatic

