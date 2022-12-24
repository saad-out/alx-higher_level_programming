#!/usr/bin/python3
"""
This script lists all states and their cities
"""


def main():
    """
    List all 'State' objects and corresponding 'City' objects,
    contained in the database hbtn_0e_101_usa
    """
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    from relationship_state import Base, State
    from relationship_city import City

    cnx = "mysql+mysqldb://{}:{}@localhost/{}".format(str(argv[1]),
                                                      str(argv[2]),
                                                      str(argv[3]))

    engine = create_engine(cnx)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))


if __name__ == '__main__':
    main()
