import psycopg2
from config import DbConfig
# Підключення до бази даних (Назва, користувач, пароль, хост, порт)
conn = psycopg2.connect(database = DbConfig.DATABASE,
                        user = DbConfig.USER,
                        password = DbConfig.PASSWORD,
                        host = DbConfig.HOST,
                        port = DbConfig.PORT)

cur = conn.cursor()

# Створення таблиці Text
cur.execute("""
    CREATE TABLE Text (
        Id SERIAL PRIMARY KEY,
        Text VARCHAR(255) NOT NULL
    );
""")
conn.commit()

# Від'єднання від бази
cur.close()
conn.close()
