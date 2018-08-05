from cornice import Service
import bcrypt

from ngse.services.utils import password_generator
from ngse.services import mailer
from ngse.services.response import generateError, generateSuccess
from ngse.models import (
    Answer,
    ApplicantAttribute,
    Category,
    CategoryStatus,
    Element,
    FormType,
    User
)

get_answers_service = Service('get answers', path='users/answers', renderer='json')


@get_answers_service.get()
def get_answers(request):  # new
    result = []
    session = request.db
    for answer in session.query(Answer):
        result.append({
            'id': answer.id,
            'text': answer.text,
            'element_id': answer.element_id,
            'user_id': answer.user_id
        })

    return result


update_answer_service = Service('update answer', path='users/answers/update', renderer='json')


@update_answer_service.post()
def update_answer(request):
    session = request.dbsession
    user_id = request.params.get('user_id')
    category_id = request.params.get('category_id')
    data = request.params.get('data')
    length = request.params.get('length')

    try:
        user = session.query(User).filter(User.id == user_id).one()
    except:
        return generateError('User id invalid')

    try:
        # change category status to answered
        category_status = session.query(CategoryStatus) \
            .filter(CategoryStatus.user_id == user_id) \
            .filter(CategoryStatus.category_id == category_id) \
            .one()
    except:
        return generateError('Category invalid')

    category_status.status = True

    for i in range(int(length)):
        answer_id = request.params.get('data[{}][id]'.format(i))
        text = request.params.get('data[{}][text]'.format(i))

        answer = session.query(Answer) \
            .filter(Answer.user_id == user_id) \
            .filter(Answer.id == answer_id) \
            .one()
        answer.text = text

        e = session.query(Element).filter(Element.id == answer.element_id).one()
        # if answer.element_id in [70, 71, 75, 76, 80, 81] and text != '':
        if (e.text == "Recommender Name" or e.text == "Recommender E-mail") and (text != ""):
            # if hindi pa existing create a new recommender
            # if answer.element_id in [70, 75, 80]:
            if e.text == "Recommender Name":
                recName = text

            # elif answer.element_id in [71, 76, 81]:
            elif e.text == "Recommender E-mail":
                attr = session.query(ApplicantAttribute) \
                    .filter(ApplicantAttribute.applicant_id == user_id).one()

                #### edit by daisy may 31
                # generated_password = 'password'
                generated_password = password_generator()
                file = open("passwords.txt", 'a')
                file.write("email: " + text + " , password: " + generated_password + "\n")
                file.close()
                ####

                password = bcrypt.hashpw(generated_password, bcrypt.gensalt())

                rec = User(name=recName, email=text, password=password, user_type_id='3')
                # session.add(rec)


                print answer.element_id
                success = False

                # if answer.element_id == 71 and attr.recommender_a == None:
                if e.name == "rec1email" and attr.recommender_a == None:
                    session.add(rec)

                    attr.recommender_a = rec.id

                    success = True
                # elif answer.element_id == 76 and attr.recommender_b == None:
                elif e.name == "rec2email" and attr.recommender_b == None:
                    session.add(rec)

                    attr.recommender_b = rec.id

                    success = True
                # elif answer.element_id == 81 and attr.recommender_c == None:
                elif e.name == "rec3email" and attr.recommender_c == None:
                    session.add(rec)

                    attr.recommender_c = rec.id

                    success = True
                if (success):
                    # todo: add send status, move mail send to some queue
                    try:
                        mailer.send_recommender_email(request.mailer, rec.name, user.name, text, generated_password)
                    except:
                        pass

                    form_type = session.query(FormType).filter(FormType.user_type_id == rec.user_type_id).one()
                    category_ids = form_type.page_sequence
                    questions = []
                    for category_id in category_ids:
                        toadd = session.query(Element).filter(Element.klass == 'question').filter(
                            Element.category_id == category_id).all()
                        for entry in toadd:
                            questions.append(entry)

                    for question in questions:
                        answer = Answer(text='', element_id=question.id, user_id=rec.id)
                        session.add(answer)

                    # initialize all status of categories_answered to False
                    for category_id in category_ids:
                        category_status = CategoryStatus(user_id=rec.id, category_id=category_id)
                        session.add(category_status)

                        ########

    return generateSuccess('Successfully updated answer')


# db_ans = session.query(Answer)\
# 		.filter(Answer.element_id == q_id)\
# 		.filter(Answer.user_id == user_id)\
# 		.all()

# if(db_ans == []):
# 	try:
# 		answer = Answer(name=curr_ans, element_id=q_id, user_id=user_id)
# 		session.add(answer)
#
# 		# return{'message': 'Answer saved', 'success':True}
# 	except:
# 		return{'message': 'Smth went wrong', 'success': False}
# else:
# 	try:
# 		# update lang here
# 		answer = session.query(Answer)\
# 				.filter(Answer.element_id == q_id)\
# 				.filter(Answer.user_id == user_id)\
# 				.first()
# 		answer.name = curr_ans
#
# 		# return{'message': 'Answer saved', 'success':True}
# 	except:
# 		return{'message': 'Smth went wrong', 'success':False}
# return{'message': 'Answer saved', 'success':True}

# def view_answer(request):

show_answer_service = Service('get answer', path='users/answers/show', renderer='json')


@show_answer_service.get()
def show_answer(request):
    session = request.dbsession
    user_id = request.params.get('user_id')
    category_id = request.params.get('category_id')

    if user_id is None or category_id is None:
        return generateError('invalid user id or category id')

    try:
        u = session.query(User).filter(User.id == user_id).one()
    except:
        return generateError('invalid user id')

    try:
        c = session.query(Category).filter(Category.id == category_id).one()
    except:
        return generateError('invalid category id')

    result = []

    answers = session.query(Answer).filter(Answer.user_id == user_id).join(Answer.element, aliased=True).filter_by(
        category_id=category_id)

    for answer in answers:
        result.append({
            'id': answer.id,
            'text': answer.text,
            'date_created': str(answer.date_created),
            'last_modifed': str(answer.last_modified),
            'element_id': answer.element_id
        })

    return result
