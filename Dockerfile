#FROM python:3
#
#RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean
#
#RUN mkdir /site
#COPY . /site/
#WORKDIR /site
#
#RUN pip install --upgrade pip
#RUN pip install django
#
#ENTRYPOINT ["python", "manage.py"]
#CMD ["python3 manage.py runserver"]

#FROM python:3.12
#
#SHELL ["/bin/bash", "-c"]
#
#RUN apt-get update && apt-get upgrade -y
#RUN pip install --upgrade pip
#RUN pip install django
#
#COPY Practic /site
#WORKDIR /site
#EXPOSE 8000
#
#RUN adduser --disabled-password service-user
#USER service-user
#
# Устанавливаем базовый образ
FROM python:3

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем все файлы из текущей директории в контейнер
COPY . /app

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Открываем порт 8000
EXPOSE 8000

# Запускаем Django сервер
# docker run -it -p 8000:8001 IMAGE запускать так
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8001"]

