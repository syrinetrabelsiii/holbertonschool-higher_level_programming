#!/usr/bin/python3
""" states Module """

import MySQLdb
import sys


def states():
    """ list states from database """
    db = MySQLdb.connect(
                            host="localhost",
                            port=3306,
                            user=sys.argv[1],
                            password=sys.argv[2],
                            db=sys.argv[3]
                            )
    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY id ASC')
    states = cur.fetchall()
    for row in states:
        print(row)
    cur.close()
    db.close()


if __name__ == '__main__':
    states()
