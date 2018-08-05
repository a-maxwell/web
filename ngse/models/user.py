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


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    date_created = Column(DateTime, nullable=False, server_default=func.now())
    last_modified = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())

    email = Column(Text, nullable=False)
    password = Column(Text, nullable=False)

    submitted = Column(Boolean, default=False)
    # meta = Column(JSON) #status can be submitted, on process, accepted, rejected

    user_type_id = Column(Integer, ForeignKey('user_types.id'), default=4)
    user_type = orm.relationship("UserType", back_populates='user')

    # applicant_attr = orm.relationship("ApplicantAttribute", back_populates='applicant')
    # rec_a = orm.relationship("ApplicantAttribute", back_populates='recommenderA')
    # rec_b = orm.relationship("ApplicantAttribute", back_populates='recommenderB')
    # rec_c = orm.relationship("ApplicantAttribute", back_populates='recommenderC')

    # applicant_attr = orm.relationship("ApplicantAttribute")
    answers = orm.relationship("Answer", back_populates="user")
