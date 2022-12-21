#!/usr/bin/python3
"""
This script that lists all states that match from the database hbtn_0e_0_usa
"""


def main():
    """
    List 'states' table of 'hbtn_0e_0_usa' database that match user input
    in ascending order by id's
    """
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()

    query = """SELECT * FROM states WHERE name LIKE '{}'
     ORDER BY id;""".format(argv[4])
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == '__main__':
    main()
