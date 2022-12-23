#!/usr/bin/python3
"""
This module lists specific state from 'hbtn_0e_6_usa' database
"""


def main():
    """
    List 'States' table object in 'hbtn_0e_usa' database
    that has a specific name passed as an argument
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

    state = session.query(State).filter(State.name == str(argv[4])).first()
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")


if __name__ == '__main__':
    main()
