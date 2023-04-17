import psycopg2
from env.config import DbConfig

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
            Text VARCHAR(255) NOT NULL
            
        );
    """)
    conn.commit()

def save_message(message):      # ����� str ��� �������� � ����
    Message = str(message)
    try:    # ��������� ������ ��� ������� ����������� �� ������� ���� �����
        cur.execute("INSERT INTO Text (Text) VALUES (%s)", (Message,))
        conn.commit()
    except psycopg2.Error as e:
        print(f"Error inserting driver: {e}")


    # cur.close()       # ³�'������� �� ����
    # conn.close()
