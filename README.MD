Цей темплейт використовується для розробки Telegram ботів з використанням бібліотеки [`aiogram v3.0+`]

### Для того, щоб почати використовувати:
1. Скопіюйте `.env.dist` в `.env` i заповніть необхідні дані.
BOT_TOKEN=BOT_TOKEN
USE_REDIS=False
DB_HOST=localhost
DB_PASS=your_password
DB_USER=your_user
DB_NAME=your_db
DB_URI=your_database_uri
2. Створіть нові хендлери.
3. **Встановлення віртуального середовища та модулів**
   1. Створіть [venv] `python -m venv venv`
   2. Встановить залежності із requirements.txt: `pip install -r requirements.txt`
   3. Запустіть проєкт з команди `python3 bot.py`
4. **Реєстрація хендлерів**
   1. Створіть у папці `handlers` новий файл з розширенням `new_file.py`
   2. Створіть новий роутер `name_router = Router()`
   3. У файлі `bot.py` імпортуйте створенний роутер `from tgbot.handlers.new_file import name_router`
   4. Додайте роутер до циклу додавання роутерів у діспатчер `for router in...`
4. **Підготовка проекту до деплою**
   1. Виконайте команду `pip freeze > requirements.txt` для запису усіх встанолених модулів
   2. У файлі `config.py` імпортуйте токени не з файлу .env а використовуйте `os`
   