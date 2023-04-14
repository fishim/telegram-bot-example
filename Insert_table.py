import psycopg2
from Create_table import conn, cur
# Підключення до бази даних (Назва, користувач, пароль, хост, порт)
# conn = psycopg2.connect(database="filonchuk",
#                         user="postgres",
#                         password="Filon2003",
#                         host="localhost",
#                         ort="5432")
# cur = conn.cursor()

# Змінна str для передачі в базу
Message = "Hello"
    
try:
    # Виконання запиту для вставки повідомлення до таблиці бази даних
    cur.execute("INSERT INTO Text (Text) VALUES (%s)", (Message,))
    conn.commit()
except psycopg2.Error as e:
    print(f"Error inserting driver: {e}")
    

