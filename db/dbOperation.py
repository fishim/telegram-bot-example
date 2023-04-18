import psycopg2
from env.config import DbConfig


def db_start():  # Підключення до бази даних (Назва, користувач, пароль, хост, порт)
    global conn, cur
    conn = psycopg2.connect(database=DbConfig.DATABASE,
                            user=DbConfig.USER,
                            password=DbConfig.PASSWORD,
                            host=DbConfig.HOST,
                            port=DbConfig.PORT)
    cur = conn.cursor()

    # Створення таблиці Text
    cur.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id SERIAL PRIMARY KEY,
            Text VARCHAR(255) NOT NULL
            
        );
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            user_id VARCHAR(255),
            user_name VARCHAR(255)
            
        );
    """)
    conn.commit()

def user_exist(user_id):
    cur.execute("""SELECT * FROM users WHERE user_id = %s""", (user_id,))
    result = cur.fetchall()
    return bool(result)

def add_user(user_id, user_name):
    cur.execute("INSERT INTO users (user_id, user_name) VALUES (%s, %s)", (user_id, user_name,))
    conn.commit()

def save_message(message):  # Змінна str для передачі в базу
    Message = str(message)
    try:    # Виконання запиту для вставки повідомлення до таблиці бази даних
        cur.execute("INSERT INTO Text (Text) VALUES (%s)", (Message,))
        conn.commit()
    except psycopg2.Error as e:
        print(f"Error inserting driver: {e}")

def close(self):
    cur.close()       # Від'єднання від бази
    conn.close()
