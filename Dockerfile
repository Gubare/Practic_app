
# Устанавливаем базовый образ питона на 240 Мб
FROM python:3-slim
#Ставим гит
RUN apt-get update && apt-get install -y git


# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем все файлы из репозитория в контейнер
RUN git clone https://github.com/Gubare/Practic_app.git .

# Устанавливаем зависимости: джанго, май скл и что-то ещё
RUN pip install -r requirements.txt

# Открываем порт 8000
EXPOSE 8000

# Запускаем Django сервер
# docker run -it -p 8000:8001 IMAGE_ID <--- запускать так
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8001"]
