import psycopg2
from Create_table import conn, cur
# ϳ��������� �� ���� ����� (�����, ����������, ������, ����, ����)
# conn = psycopg2.connect(database="filonchuk",
#                         user="postgres",
#                         password="Filon2003",
#                         host="localhost",
#                         ort="5432")
# cur = conn.cursor()

# ����� str ��� �������� � ����
Message = "Hello"
    
try:
    # ��������� ������ ��� ������� ����������� �� ������� ���� �����
    cur.execute("INSERT INTO Text (Text) VALUES (%s)", (Message,))
    conn.commit()
except psycopg2.Error as e:
    print(f"Error inserting driver: {e}")
    

