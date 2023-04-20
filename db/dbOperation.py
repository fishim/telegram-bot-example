import psycopg2
from env.config import DbConfig
from datetime import datetime


def db_start():  # ϳ��������� �� ���� ����� (�����, ����������, ������, ����, ����)
    global conn, cur
    conn = psycopg2.connect(database=DbConfig.DATABASE,
                            user=DbConfig.USER,
                            password=DbConfig.PASSWORD,
                            host=DbConfig.HOST,
                            port=DbConfig.PORT)
    cur = conn.cursor()

    # ��������� ������� Text
    cur.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id SERIAL PRIMARY KEY,
            user_id INTEGER,
            Text VARCHAR(255) NOT NULL,
            date TIMESTAMP
            
        );
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            user_id INTEGER,
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


def save_message(message):  # ����� str ��� �������� � ����
     user_id = message.chat.id
     text = message.text
     time = datetime.fromtimestamp(message.date)
     try:  # ��������� ������ ��� ������� ����������� �� ������� ���� �����
         cur.execute("INSERT INTO history (Text, user_id, date) VALUES (%s, %s, %s)", (text, user_id, time,))
         conn.commit()
     except psycopg2.Error as e:
         print(f"Error inserting driver: {e}")

def get_chat_history(message):
    # ��������� ����� ���� � ���� �����
    cur.execute("SELECT * FROM history")
    rows = cur.fetchall()
    return rows


def close(self):
    cur.close()  # ³�'������� �� ����
    conn.close()
