from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Models are imported in init_db.py to avoid circular imports
# Do not import models here
