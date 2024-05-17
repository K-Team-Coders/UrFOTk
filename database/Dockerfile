FROM postgres

RUN localedef -i ru_RU -c -f UTF-8 -A /usr/share/locale/locale.alias ru_RU.UTF-8

ENV LANG ru_RU.utf8

# Копируем файл с переменными окружения в контейнер
COPY .env /docker-entrypoint-initdb.d/

# Настраиваем переменные окружения для PostgreSQL
ENV POSTGRES_USER=$DB_USER
ENV POSTGRES_PASSWORD=$DB_PASSWORD
ENV POSTGRES_DB=$DB_NAME