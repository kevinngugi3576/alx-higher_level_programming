#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql username> \
                            <mysql password> \
                            <database name>
"""
import MySQLdb

def main():
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        password=password,
        db=dbname,
    )

    cursor = connection.cursor()
    cursor.execute("SELECT name FROM states ORDER BY id ASC")
    results = cursor.fetchall()

    for row in results:
        print(row[0])

    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()
