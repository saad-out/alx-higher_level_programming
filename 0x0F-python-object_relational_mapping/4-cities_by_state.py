#!/usr/bin/python3
"""
This script lists all cities in hbtn_0e_4_usa
"""


def main():
    """
    lists all cities from the database hbtn_0e_4_usa
    """
    import MySQLdb
    from sys import argv

    usr = str(argv[1])
    pasw = str(argv[2])
    db_name = str(argv[3])

    db = MySQLdb.connect(host='localhost', port=3306, user=usr,
                         passwd=pasw, db=db_name)
    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name \
                FROM cities \
                JOIN states ON cities.state_id = states.id \
                ORDER BY cities.id;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == '__main__':
    main()
