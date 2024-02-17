#!/usr/bin/python3
""" a script that lists all states from the database hbtn_0e_0_usa,
that takes 3 arguments: mysql username, mysql password and database name.
no argument validation needed.

Usage: script\
        <mysql UserName> <mysql PassWord> <mysql DatabaseName>\
        <mysql StateName> (searched)
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")

    cur = db.cursor()

    t_query = "SELECT * FROM {0}\
            WHERE {0}.name = '{1}'\
            ORDER BY {0}.id ASC\
            ".format("states", argv[4])
    cur.execute(t_query)

    info = cur.fetchall()
    for row in info:
        if len(row) == 2:
            print("({}, \'{}\')".format(row[0], row[1]))

    cur.close()
    db.close()
