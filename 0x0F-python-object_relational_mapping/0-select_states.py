#!/usr/bin/env python3
""" a script that lists all states from the database hbtn_0e_0_usa,
that takes 3 arguments: mysql username, mysql password and database name.
no argument validation needed.
"""
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user="root",
                         db="hbtn_0e_0_usa")

    cur = db.cursor()

    t_query = "SELECT * FROM {} ORDER BY id ASC".format("states")
    cur.execute(t_query)

    info = cur.fetchall()
    for i in info:
        print(i)

    cur.close()
    db.close()
