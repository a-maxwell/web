from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime,
    func,
    orm
)

from .base import Base
from .form_type import form_category_association


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    date_created = Column(DateTime, nullable=False, server_default=func.now())
    last_modified = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())

    form_type = orm.relationship("FormType", secondary=form_category_association,
                                 back_populates="categories")  # parent relationship

    elements = orm.relationship("Element", back_populates="category")

    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
