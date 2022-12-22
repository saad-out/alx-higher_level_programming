#!/usr/bin/python3
"""
This script lists the cities of a state
"""


def main():
    """
    takes in the name of a state as an argument
    and lists all cities of that state
    using the database hbtn_0e_4_usa
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

    cur.execute("SELECT cities.name \
                 FROM cities \
                 JOIN states \
                 ON cities.state_id = states.id \
                 WHERE states.name = %s;", (state_name, ))
    rows = cur.fetchall()
    cities = []
    for row in rows:
        cities.append(str(row[0]))
    print(', '.join(cities))

    cur.close()
    db.close()


if __name__ == '__main__':
    main()
