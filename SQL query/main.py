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
        cursor = conn.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            age INT NOT NULL
        )
        """
        cursor.execute(create_table_query)

        name = input("Enter the name: ")
        age = int(input("Enter the age: "))

        query = "INSERT INTO students (name ,age) VALUES (%s, %s)"
        cursor.execute(query, (name, age))
        conn.commit()

        print(f"{cursor.rowcount} row(s) uddated.")

except Error as e:
    print("Error while connecting to MySQL: ", e)

finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection closed.")
