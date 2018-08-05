from sqlalchemy import (
    Table,
    Column,
    Integer,
    Text,
    Boolean,
    DateTime,
    ForeignKey,
    func,
    orm
)
from sqlalchemy.dialects.postgresql import ARRAY

from .base import Base

form_category_association = Table('form_category_association', Base.metadata,
                                  Column('form_types_id', Integer, ForeignKey('form_types.id')),
                                  Column('categories_id', Integer, ForeignKey('categories.id'))
                                  )


class FormType(Base):
    __tablename__ = 'form_types'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    page_sequence = Column(ARRAY(Integer))
    date_created = Column(DateTime, nullable=False, server_default=func.now())
    last_modified = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())

    forms = orm.relationship("Form", back_populates="form_type")  # child relationship
    categories = orm.relationship("Category", secondary=form_category_association, back_populates="form_type")
    user_type_id = Column(Integer, ForeignKey('user_types.id'))

    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
