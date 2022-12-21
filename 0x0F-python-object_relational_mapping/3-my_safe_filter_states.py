#!/usr/bin/python3
"""
This script displays the 'states' table in a Safe way
"""


def main():
    """
    displays all values in the states table of hbtn_0e_0_usa
    where name matches the argument, but safe from SQL Injections
    """
    import MySQLdb
    from sys import argv

    usr = str(argv[1])
    pasw = str(argv[2])
    db_name = str(argv[3])
    state_name = str(argv[4])

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=usr, passwd=pasw, db=db_name)
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE ( %s );",
                (state_name, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == '__main__':
    main()
