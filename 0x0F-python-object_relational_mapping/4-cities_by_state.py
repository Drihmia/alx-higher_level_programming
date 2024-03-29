#!/usr/bin/python3
""" a script that lists all "cities" from the database "hbtn_0e_0_usa",

Usage: script <mysql UserName> <mysql PassWord> <mysql DatabaseName>
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")

    cur = db.cursor()
    sName = "cities"

    t_query = "SELECT {0}.id, {0}.name, {1}.name\
            FROM {0}\
            join {1}\
            on {1}.id = {0}.state_id\
            GROUP BY {0}.id\
            ORDER BY {0}.id ASC\
            ".format("cities", "states")

    cur.execute(t_query)

    info = cur.fetchall()
    for i in info:
        print(i)

    cur.close()
    db.close()
