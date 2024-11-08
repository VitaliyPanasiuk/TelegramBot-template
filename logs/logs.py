import logging
from logging.handlers import TimedRotatingFileHandler
import os
import sys

db_logger = None
bot_logger = None
error_logger = None

def log_uncaught_exceptions(ex_cls, ex, tb):
    """Глобальный обработчик необработанных исключений"""
    error_logger.error("Error", exc_info=(ex_cls, ex, tb))

# Создаем директории для логов, если их нет
def initlogging():
    global db_logger, bot_logger, error_logger
    
    if db_logger is not None and bot_logger is not None and error_logger is not None:
        return db_logger, bot_logger
    
    os.makedirs("logs/db", exist_ok=True)
    os.makedirs("logs/tg", exist_ok=True)
    os.makedirs("logs/errors", exist_ok=True)

    # Настроим формат для сообщений лога
    log_format = logging.Formatter('%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s')

    # Логгер для базы данных
    db_logger = logging.getLogger("database")
    db_logger.setLevel(logging.INFO)  # Подробный уровень логирования для базы данных

    # Обработчик с ротацией по дате для базы данных
    db_handler = TimedRotatingFileHandler("logs/db/db.log", when="midnight", interval=1)
    db_handler.setFormatter(log_format)
    db_handler.suffix = "%Y-%m-%d"  # Добавляем дату в имя файла
    db_logger.addHandler(db_handler)

    # Логгер для Telegram-бота
    bot_logger = logging.getLogger("telegram_bot")
    bot_logger.setLevel(logging.INFO)  # Общий уровень логирования для бота

    # Обработчик с ротацией по дате для Telegram-бота
    bot_handler = TimedRotatingFileHandler("logs/tg/tg.log", when="midnight", interval=1)
    bot_handler.setFormatter(log_format)
    bot_handler.suffix = "%Y-%m-%d"  # Добавляем дату в имя файла
    bot_logger.addHandler(bot_handler)
    
    error_logger = logging.getLogger("errors")
    error_logger.setLevel(logging.ERROR)  # Только ошибки

    # Обработчик с ротацией по дате для ошибок
    error_handler = TimedRotatingFileHandler("logs/errors/errors.log", when="midnight", interval=1)
    error_handler.setFormatter(log_format)
    error_handler.suffix = "%Y-%m-%d"  # Добавляем дату в имя файла
    error_logger.addHandler(error_handler)

    # Устанавливаем глобальный обработчик ошибок
    sys.excepthook = log_uncaught_exceptions
    return db_logger, bot_logger

# except Exception as e:
#     db_logger.error("Ошибка при выполнении запроса: %s", str(e))

# db_logger.info("Telegram бот запущен и готов к работе")
# db_logger.warning("Не удалось найти записи в базе данных для пользователя ID: %d", user_id)
# db_logger.error("Ошибка в Telegram боте")