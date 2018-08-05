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


class Form(Base):
    __tablename__ = 'forms'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    date_created = Column(DateTime, nullable=False, server_default=func.now())
    last_modified = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())

    date_start = Column(DateTime, nullable=False)
    date_end = Column(DateTime, nullable=False)

    form_type_id = Column(Integer, ForeignKey('form_types.id'))  # parent
    form_type = orm.relationship("FormType", back_populates="forms")  # parent relationship

    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
