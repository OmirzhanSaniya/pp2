import psycopg2

def add_or_update_contact(p_first_name, p_phone_number):
    
    conn = psycopg2.connect(host="localhost", database="suppliers", user="postgres", password="9874563210")
    cur = conn.cursor()

    cur.execute("CALL add_or_update_contact(%s, %s)", (p_first_name, p_phone_number))
    conn.commit()

    cur.close()
    conn.close()

add_or_update_contact("Alina", "2489567890")