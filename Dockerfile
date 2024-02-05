FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
#RUN python3 manage.py migrate
#RUN apt-get update && \
 #   apt-get install -y default-mysql-client && \
  #  rm -rf /var/lib/apt/lists/*

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=outils_veille_project.settings

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]