from sqlmodel import create_engine
from sqlmodel_poc.settings.constants import DATABASE_PATH

engine = create_engine(f"sqlite:///{DATABASE_PATH}")
