
import sqlite3

create_quotes = """
INSERT INTO
quotes (author,text)
VALUES
('test1', 'Программирование сегодня — это гонка разработчиков программ...'),
('test2', 'Программирование на С похоже на быстрые танцы на только...');
"""

# Подключение в БД
connection = sqlite3.connect("test.db")
# Создаем cursor, он позволяет делать SQL-запросы
cursor = connection.cursor()
# Выполняем запрос:
cursor.execute(create_quotes)
# Фиксируем выполнение(транзакцию)
connection.commit()
# Закрыть курсор:
cursor.close()
# Закрыть соединение:
connection.close()

