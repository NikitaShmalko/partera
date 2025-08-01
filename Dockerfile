# Шаг 1: Используем официальный Python образ
FROM python:3.10-slim

# Шаг 2: Создаем рабочую директорию для проекта
WORKDIR /app

# Шаг 3: Копируем файл requirements.txt в контейнер
COPY requirements.txt /app/

# Шаг 4: Устанавливаем зависимости из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Шаг 5: Копируем все файлы проекта в контейнер
COPY . /app

# Шаг 6: Запускаем тесты с сохранением отчёта Allure
CMD ["pytest", "--alluredir=/app/allure-results"]