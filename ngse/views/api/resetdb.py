from cornice import Service
from ngse.services.validators import has_admin_rights

from ngse.models import (
    Answer,
    ApplicantAttribute,
    CategoryStatus,
    User
)
# todo: move to cli script, set cascade delete in db

resetdb = Service('', path='delete_all')


@resetdb.get(validators=(has_admin_rights))
def reset_database(request):
    # if admin
    session = request.dbsession
    # problem: does not delete the id sequence
    for answer in session.query(Answer).all():
        session.delete(answer)
    for attrib in session.query(ApplicantAttribute).all():
        session.delete(attrib)
    for status in session.query(CategoryStatus).all():
        session.delete(status)
    for user in session.query(User).filter(User.user_type_id > 2).all():
        session.delete(user)

    session.commit()
    return {'success': True}
