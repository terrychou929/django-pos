#!/bin/sh

# 等待 MySQL 服務準備好
until mysqladmin ping -h"$DATABASE_HOST" -u"$DATABASE_USER" -p"$DATABASE_PASSWORD" --silent; do
    echo "Waiting for MySQL to be ready..."
    sleep 2
done

echo "MySQL is ready, proceeding with migrations and server startup..."

# 執行遷移和啟動伺服器
python manage.py migrate
python manage.py runserver 0.0.0.0:8000