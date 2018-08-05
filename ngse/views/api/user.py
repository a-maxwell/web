from cornice import Service
from email.utils import parseaddr
from sqlalchemy.orm.exc import (NoResultFound, MultipleResultsFound)
import bcrypt
import jwt

from ngse.services import mailer
from ngse.services.validators import has_admin_rights, has_token
from ngse.services.utils import password_generator, decode
from ngse.services.response import (
    generateError,
    generateSuccess,
    generateToken
)
from ngse.models import (
    Answer,
    ApplicantAttribute,
    CategoryStatus,
    Element,
    FormType,
    User
)

get_users_service = Service('get users list', path='users', renderer='json')


@get_users_service.get()
def get_users(request):
    d = []
    session = request.dbsession
    for u in session.query(User):
        if u.user_type.name == "ERDT Applicant" or u.user_type.name == "Non-ERDT Applicant":
            _u = session.query(ApplicantAttribute).filter(ApplicantAttribute.applicant_id == u.id).first()
            rec_a = session.query(User).filter(User.id == _u.recommender_a).all()
            rec_b = session.query(User).filter(User.id == _u.recommender_b).all()
            rec_c = session.query(User).filter(User.id == _u.recommender_c).all()

            rec = [rec_a, rec_b, rec_c]
            for r in rec:
                if r != []:
                    rec[rec.index(r)] = r[0].name
                else:
                    rec[rec.index(r)] = "None"
            d.append({
                'id': int(u.id),
                'name': u.name,
                'email': u.email,
                'user_type': u.user_type.name,
                'level': _u.level,
                'program': _u.program,
                'application_status': _u.application_status,
                'validation_status': _u.validation_status,
                'recommender1': rec[0],
                'recommender2': rec[1],
                'recommender3': rec[2],
                'date_created': str(u.date_created),
                'last_modified': str(u.last_modified)
            })
        else:
            d.append({
                'id': int(u.id),
                'name': u.name,
                'email': u.email,
                'user_type': u.user_type.name,
                'date_created': str(u.date_created),
                'last_modified': str(u.last_modified)
            })
    return d


verify_service = Service('verify', path='users/verify', renderer='json')


@verify_service.post()
def verify_user(request):
    token = request.params.get('token', None)

    if token is None:
        return generateError('Token is missing', {'expired': False})

    try:
        payload = decode(token)
    except jwt.ExpiredSignatureError:
        return generateError('Token has expired', {'expired': True})
    except:
        return generateError('Token is invalid', {'expired': False})

    return generateSuccess('Token is valid', {'expired': False})


login_service = Service('login', path='users/login', renderer='json')


@login_service.post()
def login_user(request):
    email = request.params.get('email', None)
    password = request.params.get('password', None)
    form_start = request.params.get('date_start')
    form_end = request.params.get('date_end')
    user_form_start = request.params.get('date_created')
    user_form_end = request.params.get('last_modified')
    session = request.dbsession
    
    #if user_form_start < form_start:
    #    return generateError('Form is not yet open')
    if user_form_start != form_end:
        return generateError('Form has closed, you can no longer submit your form online.')
    
    if email is None or password is None:
        return generateError('Invalid email and password combination')

    try:
        user = session.query(User).filter(User.email == email).one()
        pwd = bcrypt.hashpw(password.encode('UTF_8'), user.password.encode('UTF_8'))

        if (pwd != user.password):
            return generateError('Invalid email and password combination')

    # todo: how this possibly could happen?
    except MultipleResultsFound:
        users = session.query(User).filter(User.email == email).all()
        user = None
        for u in users:
            pwd = bcrypt.hashpw(password.encode('UTF_8'), u.password.encode('UTF_8'))
            if (pwd == u.password):
                user = u
                break
        if user == None:
            return generateError('Invalid email and password combination')

    except NoResultFound:
        return generateError('Invalid email and password combination')

    return generateSuccess('Welcome, {}!'.format(user.name), {'token': generateToken(user)})


create_user_service = Service('create user', path='users/create', renderer='json')


@create_user_service.post()
def create_user(request):
    # check for required params, return error if incomplete
    session = request.dbsession
    email = request.params.get('email', None)
    last = request.params.get('last', None)
    given = request.params.get('given', None)
    middlemaiden = request.params.get('middlemaiden', None)
    level = request.params.get('level', None)
    fullname = '{} {}'.format(given, last)

    parsed = parseaddr(email)

    if parsed[1] == "":
        return generateError('Invalid email')
    ##########
    # EDIT: may 31 - daisy
    # generated_password = 'password'

    generated_password = password_generator()

    # just for debugging purposes. will delete these lines eventually

    file = open("passwords.txt", 'a')
    file.write("email: " + email + " , password: " + generated_password + "\n")
    file.close()

    password = bcrypt.hashpw(generated_password, bcrypt.gensalt())

    if email is None or last is None or given is None or middlemaiden is None:
        return generateError('Field is missing')

    # check if user is not recommender email is linked to an account
    u = session.query(User).filter(User.email == email).all()
    if (level != 3 and len(u) > 0):
        return generateError('E-mail is already in use')

    try:
        if level is None:
            u = User(name=fullname, email=email, password=password)
        else:
            u = User(name=fullname, email=email, password=password, user_type_id=int(level))
    except:
        return generateError('Something weird happened!')

    # todo: add send status, move mail send to some queue
    try:
        mailer.send_credentials_email(request.mailer, given, email, generated_password)
    except:
        pass

    session.add(u)
    session.flush()

    if int(level) in [3, 4, 5]:

        #######
        # add a row in ApplicantAttribute Table
        if level == '4':
            row = ApplicantAttribute(scholarship=False, applicant_id=u.id)
        elif level == '5':
            row = ApplicantAttribute(scholarship=True, applicant_id=u.id)

        if int(level) in [4, 5]:
            session.add(row)

        #######

        # create answer
        form_type = session.query(FormType).filter(FormType.user_type_id == u.user_type_id).one()
        # forms = session.query(Form).filter(Form.form_type_id == form_type.id).all()
        # for f in forms:
        # 	started = is_past(str(f.date_start))
        # 	ended = is_past(str(f.date_end))

        # 	status = 'idle' if (not started) else ( 'expired' if (ended) else 'ongoing' )

        # 	if (status is 'ongoing'):
        # 		form = f
        # 		break
        category_ids = form_type.page_sequence
        questions = []

        for category_id in category_ids:
            toadd = session.query(Element).filter(Element.klass == 'question').filter(
                Element.category_id == category_id).all()
            for entry in toadd:
                questions.append(entry)

        for question in questions:
            answer = Answer(text='', element_id=question.id, user_id=u.id)
            if question.default:
                answer.text = question.default
            session.add(answer)
            #      session.commit()

        # initialize all status of categories_answered to False
        for category_id in category_ids:
            category_status = CategoryStatus(user_id=u.id, category_id=category_id)
            session.add(category_status)

    return generateSuccess('Welcome, {}!'.format(fullname), {'token': generateToken(u)})


delete_user_service = Service('delete user', path='users/delete', renderer='json')


# tdoo: replace with post or delete http method
@delete_user_service.get()
def delete_user(request):
    '''
    input id of user accessing endpoint, id of user to delete, type of user
    input step number for testing
    '''
    session = request.dbsession
    step = int(request.params.get('step', 0))  # variable for testing
    user_id = request.params.get('user_id', None)
    _id = request.params.get('id', None)

    if user_id is None or _id is None:  # user_id was not passed
        return generateError('Required field is missing')

    try:
        user_id = int(user_id)
    except ValueError:  # user_id not an integer
        return generateError('user_id is invalid')

    if user_id < 1 or user_id > 2147483647:  # user_id beyond range
        return generateError('user_id is out of bounds')

    try:
        _id = int(_id)
    except ValueError:  # id not an integer
        return generateError('id is invalid')

    if _id < 1 or _id > 2147483647:
        return generateError('id is out of bounds')

    try:
        user = session.query(User).filter(User.id == user_id).one()
    except NoResultFound:  # user_id not found in database
        return generateError('User accessing does not exist')

    user_type = user.user_type_id

    if ((user_type != 1) and (user_id != _id)):  # not admin deleting different id
        return generateError('Unauthorized')

    if ((user_type == 1) and (user_id == _id)):  # admin deleting admin id
        return generateError('Cannot delete admin account')

    try:
        other_user = session.query(User).filter(User.id == _id).one()
    except NoResultFound:  # id not found in database
        return generateError('User ')

    if step == 5:
        return {'message': 'other user exists'}


show_user_service = Service('get user', path='users/show', renderer='json')


@show_user_service.get()
def show_user(request):
    session = request.dbsession
    user_id = request.params['user_id']
    try:
        user = session.query(User) \
            .filter(User.id == user_id) \
            .one()
    except:
        return generateError('user id is invalid')

    d = {
        'name': user.name,
        'date_created': str(user.date_created),
        'last_modified': str(user.last_modified),
        'email': user.email,
        'user_type_id': user.user_type_id
    }

    if (user.user_type_id in [4, 5]):
        # d['application_status'] = user.application_status
        attrib = session.query(ApplicantAttribute).filter(ApplicantAttribute.applicant_id == user_id).one()
        d['validation_status'] = attrib.validation_status
        d['application_status'] = attrib.application_status
        d['answered_pos'] = attrib.answered_pos

        d['level'] = attrib.level
        d['program'] = attrib.program
        d['program_type'] = attrib.program_type
        d['student_type'] = attrib.student_type
        d['choice_1'] = attrib.choice_1
        d['choice_2'] = attrib.choice_2
        d['choice_3'] = attrib.choice_3
        d['adviser'] = attrib.adviser
        d['start_of_study'] = attrib.start_of_study
        d['year'] = attrib.year
        d['other_scholarship'] = attrib.other_scholarship
        d['other_scholarship_name'] = attrib.other_scholarship_name

        # get recommender info

        d['recommenders'] = []
        if (attrib.recommender_a is None or attrib.recommender_b is None or attrib.recommender_c is None):
            for i in range(3):
                d['recommenders'].append({'name': 'Not yet assigned'})
        else:
            for recommender in [(attrib.recommender_a, attrib.rec_a), (attrib.recommender_b, attrib.rec_b),
                                (attrib.recommender_c, attrib.rec_c)]:
                info = {
                    'id': recommender[0],
                    'name': recommender[1].name,
                    'status': True
                }

                category_statuses = session.query(CategoryStatus) \
                    .filter(CategoryStatus.user_id == recommender[0]) \
                    .all()

                for category_status in category_statuses:
                    if not category_status.status:
                        info['status'] = False
                        break

                d['recommenders'].append(info)

    if (user.user_type_id in [3, 4, 5]):
        d['submitted'] = user.submitted

        categories = session.query(CategoryStatus) \
            .filter(CategoryStatus.user_id == user_id) \
            .all()

        d['answered'] = []

        for category in categories:
            d['answered'].append({
                'id': category.id,
                'category_id': category.category_id,
                'status': category.status
            })

        answers = session.query(Answer) \
            .filter(Answer.user_id == user_id) \
            .all()

        d['answers'] = []

        for answer in answers:
            d['answers'].append({
                'id': answer.id,
                'category_id': answer.element.category_id,
                'element_id': answer.element_id,
                'name': answer.text
            })

    return d


update_user_service = Service('update user', path='users/update', renderer='json')


@update_user_service.post()
def update_user(request):
    session = request.dbsession
    token = request.authorization[1]
    payload = decode(token)
    user_id = payload['sub']

    try:
        user = session.query(User) \
            .filter(User.id == user_id) \
            .one()
    except:
        return generateError('Db error. Contact site administrator')

    submitted = request.params.get('submitted', None)
    password = request.params.get('password', None)
    appstat = request.params.get('application_status', None)
    valstat = request.params.get('validation_status', None)

    if not submitted is None:
        user.submitted = submitted

        return generateSuccess('user submission successful')

    if not password is None:
        user.password = bcrypt.hashpw(password, bcrypt.gensalt())

        return generateSuccess('password successfully changed')

    if not appstat is None:
        user.application_status = appstat

        return generateSuccess('application status successfully changed')

    if not valstat is None:
        user.validation_status = valstat

        return generateSuccess('validation status successfully changed')

    try:
        user_attribs = session.query(ApplicantAttribute) \
            .filter(ApplicantAttribute.applicant_id == user_id) \
            .one()
    except:
        return generateError('Db error. Contact site administrator')

    attribs = [
        'level',
        'program',
        'program_type',
        'student_type',
        'choice_1',
        'choice_2',
        'choice_3',
        'adviser',
        'start_of_study',
        'year',
        'other_scholarship',
        'other_scholarship_name'
    ]

    for key in attribs:
        value = request.params.get('user[{}]'.format(key))
        if (key == 'level'):
            user_attribs.level = value
        if (key == 'program'):
            user_attribs.program = value
        if (key == 'program_type'):
            user_attribs.program_type = value
        if (key == 'student_type'):
            user_attribs.student_type = value
        if (key == 'choice_1'):
            user_attribs.choice_1 = value
        if (key == 'choice_2'):
            user_attribs.choice_2 = value
        if (key == 'choice_3'):
            user_attribs.choice_3 = value
        if (key == 'adviser'):
            user_attribs.adviser = value
        if (key == 'start_of_study'):
            user_attribs.start_of_study = value
        if (key == 'year'):
            user_attribs.year = value
        if (key == 'other_scholarship'):
            user_attribs.other_scholarship = value
        if (key == 'other_scholarship_name'):
            user_attribs.other_scholarship_name = value

    user_attribs.answered_pos = True

    return {'success': True}


change_application_status_service = Service('Change application status', path='users/{id}/application/status',
                                            renderer='json')


@change_application_status_service.post(validators=(has_admin_rights, has_token))
def change_application_status(request):
    session = request.dbsession
    user_id = request.matchdict['id']
    status = request.params['status']

    try:
        attrib = session.query(ApplicantAttribute).filter(ApplicantAttribute.applicant_id == user_id).one()
    except NoResultFound:
        return generateError('User is not an applicant or no attribute found')
    except:
        return generateError('Unexpected Db error')

    attrib.application_status = status

    return generateSuccess('Application status saved')


change_validation_status_service = Service('Change validation status', path='users/{id}/validation/status',
                                           renderer='json')


@change_validation_status_service.post(validators=(has_admin_rights, has_token))
def change_validation_status(request):
    session = request.dbsession
    user_id = request.matchdict['id']
    status = request.params['status']

    try:
        attrib = session.query(ApplicantAttribute).filter(ApplicantAttribute.applicant_id == user_id).one()
    except:
        return generateError('user id is invalid')

    attrib.validation_status = status

    return generateSuccess('Validation status saved')
