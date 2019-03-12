from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# Module state
engine = None
Base = None

# Error messages
UNINITIALIZED='Database settings have not been configured'

def config(connection_str):
    global engine, Base
    engine = create_engine(connection_str)
    Base = declarative_base(engine)

def get_engine():
    if engine is None:
        raise RuntimeError (UNINITIALIZED)
    return engine

def get_base():
    if Base is None:
        raise RuntimeError (UNINITIALIZED)
    return Base
