import psycopg2

def delete_user_data():
    try:
        conn = psycopg2.connect(host="localhost", database="suppliers", user="postgres", password="9874563210")
        cur = conn.cursor()

        search_term = input("Введите имя пользователя или номер телефона для удаления: ")

        cur.execute("CALL delete_user_data(%s)", (search_term,))
        conn.commit()
        print("Процедура успешно выполнена.")
    except psycopg2.DatabaseError as e:
        print(f"Ошибка выполнения процедуры: {e}")
    finally:
        if conn is not None:
            cur.close()
            conn.close()

delete_user_data()