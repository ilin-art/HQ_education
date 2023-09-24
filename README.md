# HQ_education

Суть задания заключается в проверке знаний построения связей в БД и умение правильно строить запросы без ошибок N+1.

### Установка

1. Клонируйте репозиторий на вашу локальную машину:
```
git clone https://github.com/ilin-art/HQ_education.git
```
2. Перейдите в директорию проекта:
```
cd HQ_education
```
3. Установите зависимости:
```
pip install -r requirements.txt
```
4. Выполните миграции:
```
python manage.py migrate
```
5. Запустите сервер разработки:
```
python manage.py runserver
```
6. Создайте суперпользователя:
```
python manage.py createsuperuser
```
