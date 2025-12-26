# Dockerfile
FROM python:3.13-slim

# Установка зависимостей ОС
RUN apt-get update && apt-get install -y \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Установка Poetry (опционально, но мы используем pip)
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код
COPY . .

# Создаём миграции и суперпользователя (опционально)
# RUN python manage.py migrate

# Порт, который будет слушать контейнер
EXPOSE 8000

# Запуск сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]