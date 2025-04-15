import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='@ditya000',
        database='user'
    )

    if conn.is_connected():
        print("Connected to MySQL database!")

        student_id = int(input("Enter student ID to update: "))
        new_name = input("Enter the name: ")
        new_age = int(input("Enter the age: "))

        query = """
            UPDATE students
            SET name = %s, age = %s
            WHERE id = %s
        """

        cursor = conn.cursor()
        cursor.execte(query, (new_name, new_age, student_id))
        conn.commit()

        print(f"{cursor.rowcount} row(s) uddated.")

except Error as e:
    print("Error while connecting to MySQL: ", e)

finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection closed.")
