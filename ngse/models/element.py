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
from sqlalchemy.dialects.postgresql import ARRAY, JSON

from .base import Base


class Element(Base):
    __tablename__ = 'elements'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    date_created = Column(DateTime, nullable=False, server_default=func.now())
    last_modified = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())

    category_id = Column(Integer, ForeignKey('categories.id'))  # parent
    category = orm.relationship("Category", back_populates="elements")  # parent relationship

    # form_type_id = Column(Integer, ForeignKey('form_types.id')) # parent
    # form_type = orm.relationship("FormType", back_populates="questions") # parent relationship

    text = Column(Text, nullable=False)
    klass = Column(Text, nullable=False, default='question')
    kind = Column(Text, nullable=False, default='text')
    width = Column(Integer, nullable=False, default=16)
    choices = Column(ARRAY(Text))
    default = Column(Text)
    required = Column(Boolean)

    meta = Column(JSON)

    answers = orm.relationship("Answer", back_populates="element")

    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
