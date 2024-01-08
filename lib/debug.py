#!/usr/bin/env python3

from sqlalchemy import create_engine

from sqlalchemy_sandbox import Student,Base

engine = create_engine('sqlite:///students.db')

if __name__ == '__main__':
    engine = create_engine('sqlite:///students.db')
    Base.metadata.create_all(engine)
