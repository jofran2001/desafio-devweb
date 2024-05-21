FROM mysql

ENV MYSQL_DATABASE=user
ENV MYSQL_PASSWORD=Joãomysql
ENV MYSQL_ROOT_PASSWORD=root

COPY init.sql /docker-entrypoint-initdb.d/
