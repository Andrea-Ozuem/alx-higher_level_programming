#!/usr/bin/python3

"""a script that lists all cities of a state that matches the input state"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities INNER JOIN states ON \
                 cities.state_id = states.id WHERE states.name = %s \
                 ORDER BY cities.id", (sys.argv[4],))
    rows = cur.fetchall()
    l_row = [ele for row in rows for ele in row]
    print(", ".join(l_row))
    cur.close()
    db.close()
