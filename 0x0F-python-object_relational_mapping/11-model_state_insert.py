#!/usr/bin/python3
"""
This script inserts new row in 'States'
"""


def main():
    """
    Insert new row into 'States' table of a given database
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

    new_state = State(name='Louisiana')
    session.add(new_state)
    state = session.query(State).filter_by(name='Louisiana').first()
    print(state.id)
    session.commit()


if __name__ == '__main__':
    main()
