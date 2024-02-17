#!/usr/bin/python3
""" a script that lists all states from the database hbtn_0e_0_usa,
that takes 3 arguments: mysql username, mysql password and database name.
no argument validation needed.

Usage: script <mysql UserName> <mysql PassWord> <mysql DatabaseName>
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")

    cur = db.cursor()

    t_query = "SELECT * FROM {0}\
            WHERE {0}.name LIKE 'N%'\
            ORDER BY {0}.id ASC\
            ".format("states")

    cur.execute(t_query)

    info = cur.fetchall()
    for i in info:
        print(i)

    cur.close()
    db.close()
