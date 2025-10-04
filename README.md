# Сайт охраны
Это внутренний инструмент в виде веб-приложения для просмотра данных по пропускам.

# Установка
1. Клонировать репозиторий: 
`git clone https://github.com/cedradeff/django-orm-watching-storage-part-2`
2. Установить зависимости:
`pip install -r requirements.txt`
3. Заполнить данные для подключения к БД в файле `.env`:
Занести в переменную DB_URL URL (пример для postgres БД):
`postgres://USER:PASSWORD@HOST:PORT/NAME`
4. Режим DEBUG по умолчанию отключен. Для включения занести в переменную `DEBUG` в .env значения True.

# Запуск
Запустить сайт локально командой:
```bash
python manage.py runserver 0.0.0.0:8000
```
