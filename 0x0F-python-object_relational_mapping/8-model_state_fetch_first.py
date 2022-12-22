#!/usr/bin/python3
"""
This module lists first state from 'hbtn_0e_6_usa' database
"""


def main():
    """
    List first of 'States' table objects in 'hbtn_0e_usa' database
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

    state = session.query(State).first()
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")


if __name__ == '__main__':
    main()
