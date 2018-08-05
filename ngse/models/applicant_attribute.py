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


class ApplicantAttribute(Base):
    __tablename__ = 'applicant_attrs'

    id = Column(Integer, primary_key=True)
    date_created = Column(DateTime, nullable=False, server_default=func.now())
    last_modified = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())

    scholarship = Column(Boolean, nullable=False, default=False)
    application_status = Column(Text, nullable=False, default='None')
    validation_status = Column(Text, nullable=False, default='None')

    level = Column(Text)
    program = Column(Text)
    program_type = Column(Text)
    student_type = Column(Text)
    choice_1 = Column(Text)
    choice_2 = Column(Text)
    choice_3 = Column(Text)
    adviser = Column(Text)

    start_of_study = Column(Text)
    year = Column(Text)
    other_scholarship = Column(Text)
    other_scholarship_name = Column(Text)

    answered_pos = Column(Boolean, default=False)

    recommender_a = Column(Integer, ForeignKey('users.id'))
    recommender_b = Column(Integer, ForeignKey('users.id'))

    recommender_c = Column(Integer, ForeignKey('users.id'))

    applicant_id = Column(Integer, ForeignKey('users.id'))
    # applicant = orm.relationship("User", back_populates='applicant_attr')

    applicant = orm.relationship("User", foreign_keys='ApplicantAttribute.applicant_id')
    rec_a = orm.relationship("User", foreign_keys='ApplicantAttribute.recommender_a')
    rec_b = orm.relationship("User", foreign_keys='ApplicantAttribute.recommender_b')
    rec_c = orm.relationship("User", foreign_keys='ApplicantAttribute.recommender_c')
