#!/usr/bin/python3
""" a script that lists all states from the database hbtn_0e_0_usa,
that takes 3 arguments: mysql username, mysql password and database name.
no argument validation needed.

Usage: script UserName PassWord DatabaseName StateName (searched)
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")

    cur = db.cursor()
    sName = argv[4]

    # handling the case where the sName contain a single quote
    index = sName.find(";")
    if (index >= 0):
        sName = sName[:index]

    t_query = "SELECT * FROM {0} WHERE name='{1}' ORDER BY {0}.id ASC".format(
            "states", sName)
    cur.execute(t_query)

    info = cur.fetchall()
    for i in info:
        print(i)

    cur.close()
    db.close()
