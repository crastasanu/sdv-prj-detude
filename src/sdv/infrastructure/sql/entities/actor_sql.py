
from src.sdv.infrastructure.sql.entities import Base
from sqlalchemy import SMALLINT, VARCHAR, TIMESTAMP, Column


class ActorSQL(Base):
    __tablename__ = "actor"

    id = Column("actor_id", SMALLINT, primary_key=True)
    first_name = Column("first_name", VARCHAR(45))
    last_name = Column("last_name", VARCHAR(45))
    last_update = Column('last_update', TIMESTAMP)
