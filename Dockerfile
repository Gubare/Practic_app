
# Устанавливаем базовый образ питона на 150 Мб
FROM python:3-alpine3.16


# Устанавливаем рабочую директорию в контейнере
COPY . /app
WORKDIR /app


# Устанавливаем зависимости: джанго, май скл и что-то ещё
RUN pip install -r requirements.txt

# Открываем порт 8000
EXPOSE 8000

CMD  "python3" "manage.py" "runserver" "0.0.0.0:8001"