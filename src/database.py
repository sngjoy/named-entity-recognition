from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "postgresql://{user}:{password}@{postgresserver}/{db}"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@localhost/spacy_ner"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=True, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """allows a route to use the same session through a
    request and then close it when the request is finished
    """
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()
