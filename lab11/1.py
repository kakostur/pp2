import psycopg2

params = {
    'host': 'localhost',
    'database': 'suppliers',
    'user': 'postgres',
    'password': '1234',
    'port': '5433'
}

def get_records_by_pattern(pattern_text):
    conn = psycopg2.connect(**params)
    cursor = conn.cursor()
    cursor.execute("SELECT name, number FROM phonebook WHERE name ILIKE %s OR number LIKE %s", ('%' + pattern_text + '%', '%' + pattern_text + '%'))
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    return records

def insert_or_update_user(name_param, phone_param):
    conn = psycopg2.connect(**params)
    cursor = conn.cursor()
    cursor.execute("DO $$ BEGIN IF EXISTS (SELECT 1 FROM phonebook WHERE name = %s) THEN UPDATE phonebook SET number = %s WHERE name = %s; ELSE INSERT INTO phonebook (name, number) VALUES (%s, %s); END IF; END $$", (name_param, phone_param, name_param, name_param, phone_param))
    conn.commit()
    cursor.close()
    conn.close()

def insert_many_users(users_data):
    conn = psycopg2.connect(**params)
    cursor = conn.cursor()
    cursor.execute("CREATE TEMP TABLE temp_users (name TEXT, number TEXT)")
    conn.commit()

    for user_data in users_data:
        cursor.execute("INSERT INTO temp_users (name, number) VALUES (%s, %s)", user_data)
    conn.commit()

    cursor.execute("CREATE TEMP TABLE incorrect_data AS SELECT name, number FROM temp_users WHERE LENGTH(number) <> 10 OR number ~ '\D'")
    conn.commit()

    cursor.execute("INSERT INTO phonebook (name, number) SELECT name, number FROM temp_users WHERE (name, number) NOT IN (SELECT name, number FROM incorrect_data)")
    conn.commit()

    cursor.execute("DROP TABLE temp_users")
    conn.commit()

    cursor.close()
    conn.close()

if __name__ == "__main__":
    pattern = 'John'
    print("Records matching pattern:")
    print(get_records_by_pattern(pattern))

    new_user_name = 'John Doe'
    new_user_number = '1234567890'
    insert_or_update_user(new_user_name, new_user_number)

    new_users_data = [
        ('Alice', '1234567890'),
        ('Bob', '2345678901'),
        ('Charlie', '3456789012')
    ]
    insert_many_users(new_users_data)
