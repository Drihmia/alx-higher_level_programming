#!/usr/bin/python3
""" a script that takes in the name of a state as an argument and lists all
"cities" of that state, using the database "hbtn_0e_4_usa"

Usage: script\
        <mysql UserName> <mysql PassWord> <mysql DatabaseName>\
        <mysql StateName> (searched + safe from MySQL injection)
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

    t_query = "SELECT {0}.name\
            FROM {0}\
            join {1}\
            on {0}.state_id = {1}.id\
            WHERE {1}.name = '{2}'\
            GROUP BY {0}.id\
            ORDER BY {0}.id ASC\
            ".format("cities", "states", sName)

    cur.execute(t_query)

    info = cur.fetchall()
    st = ""
    for i in info:
        st += i[0] + ", "
    print(st[:-2])

    cur.close()
    db.close()
