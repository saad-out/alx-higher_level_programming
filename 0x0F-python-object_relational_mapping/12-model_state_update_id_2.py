#!/usr/bin/python3
"""
This script update a row in 'States'
"""


def main():
    """
    update the name column of a row in 'States' table of a given database
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

    state = session.query(State).filter_by(id=2).first()
    state.name = 'New Mexico'
    session.commit()


if __name__ == '__main__':
    main()
