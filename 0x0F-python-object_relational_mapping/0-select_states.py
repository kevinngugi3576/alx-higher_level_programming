#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql username> \
                            <mysql password> \
                            <database name>
"""
import MySQLdb
import sys

def main():
    host = "localhost"
    port = 3306
    user = sys.argv[2]
    password = "root"
    db = "alx_python"

    connection = MySQLdb.connect(host=host, port=port, user=user, password=password, db=db)
    cursor = connection.cursor()

    cursor.execute("SELECT name FROM states")
    for row in cursor:
        print(row[0])

if __name__ == "__main__":
    main()
