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


class CategoryStatus(Base):
    __tablename__ = 'category_status'

    id = Column(Integer, primary_key=True)
    date_created = Column(DateTime, nullable=False, server_default=func.now())
    last_modified = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())

    status = Column(Boolean, nullable=False, default=False)

    user_id = Column(Integer, ForeignKey('users.id'))  # parent
    # user = orm.relationship("User", back_populates='answers') # parent relationship

    category_id = Column(Integer, ForeignKey('categories.id'))  # parent
    # category = orm.relationship("Category", back_populates="elements") #parent relationship
