#!/usr/bin/python3

"""  A list of all states from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    My_connect = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        connect=argv[3],
        charset="utf8")

    ora = My_connect.cursor()
    ora.execute("SELECT * FROM states ORDER BY id ASC")

    for row in ora.fetchall():
        print(row)
    ora.close()
    My_connect.close()