import psycopg2
from config import DbConfig
# ϳ��������� �� ���� ����� (�����, ����������, ������, ����, ����)
conn = psycopg2.connect(database = DbConfig.DATABASE,
                        user = DbConfig.USER,
                        password = DbConfig.PASSWORD,
                        host = DbConfig.HOST,
                        port = DbConfig.PORT)

cur = conn.cursor()

# ��������� ������� Text
cur.execute("""
    CREATE TABLE Text (
        Id SERIAL PRIMARY KEY,
        Text VARCHAR(255) NOT NULL
    );
""")
conn.commit()

# ³�'������� �� ����
cur.close()
conn.close()
