#!/usr/bin/python3
"""
This script deletes specific rows in 'States'
"""


def main():
    """
    delete rows with name that contain 'a'
    in 'States' table of a given database
    """
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from sys import argv

    from model_state import Base, State

    cnx = "mysql+mysqldb://{}:{}@localhost/{}".format(str(argv[1]),
                                                      str(argv[2]),
                                                      str(argv[3]))

    engine = create_engine(cnx)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like("%a%")).all()
    for state in states:
        session.delete(state)
    session.commit()


if __name__ == '__main__':
    main()
