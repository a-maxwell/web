from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime,
    ForeignKey,
    func,
    orm
)

from .base import Base


class Answer(Base):
    __tablename__ = 'answers'

    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=False)
    date_created = Column(DateTime, nullable=False, server_default=func.now())
    last_modified = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())

    element_id = Column(Integer, ForeignKey('elements.id'))  # parent
    element = orm.relationship("Element", back_populates='answers')  # parent relationship

    user_id = Column(Integer, ForeignKey('users.id'))  # parent
    user = orm.relationship("User", back_populates='answers')  # parent relationship

    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
