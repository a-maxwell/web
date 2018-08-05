from sqlalchemy import (
    Column,
    Integer,
    Text,
    Boolean,
    DateTime,
    ForeignKey,
    func,
    orm
)

from .base import Base


class UserType(Base):
    __tablename__ = 'user_types'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    # date_created = Column(DateTime, nullable=False, server_default=func.now())
    # last_modified = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())

    user = orm.relationship("User", back_populates='user_type')

    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
