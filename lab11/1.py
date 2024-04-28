import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(host="localhost", database="suppliers", user="postgres", password="9874563210")
cur = conn.cursor()

def search_contacts(pattern):
    cur.execute(sql.SQL("SELECT * FROM phonebook WHERE first_name LIKE %s OR last_name LIKE %s OR phone_number LIKE %s"), 
                [f"%{pattern}%", f"%{pattern}%", f"%{pattern}%"])
    return cur.fetchall()

def search_contacts_from_input():
    pattern = input("Введите шаблон для поиска контактов: ")
    search_result = search_contacts(pattern)
    print("Результат поиска:", search_result)

search_contacts_from_input()

cur.close()
conn.close()