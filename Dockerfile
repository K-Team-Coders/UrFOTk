FROM python:3.10-alpine

COPY . .

WORKDIR ./

COPY ./fastApi ./fastApi
# copy file requirements.txt to workdir
# Копируем файл зависимостей в рабочую директорию внутри контейнера
COPY ./pyproject.toml ./pyproject.toml

# Run pip and install requiremnts withous localy saved
# Устанавливаем зависимости и не сохраняем их локально
RUN pip install --no-cache-dir --upgrade poetry \
    && poetry config virtualenvs.create false \
    && rm -rf $(poetry config cache-dir)/{cache,artifacts}

COPY . .

EXPOSE 8000
