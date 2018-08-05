from reportlab.pdfgen import canvas
from pyramid.response import FileResponse
from cornice import Service

from ngse.services import pdf
from ngse.services.utils import is_past
from ngse.services.validators import has_admin_rights, has_token, has_form_id
from ngse.services.response import generateError, generateSuccess
from ngse.models import (
    Answer,
    Element,
    Form,
    FormType,
    User
)

get_forms_service = Service('get forms', path='forms', renderer='json')


@get_forms_service.get()
def get_forms(request):
    d = []
    session = request.dbsession
    for f in session.query(Form):
        started = is_past(str(f.date_start))
        ended = is_past(str(f.date_end))

        status = 'idle' if (not started) else ('expired' if (ended) else 'ongoing')

        d.append({
            'id': int(f.id),
            'name': f.name,
            'user': f.form_type.user_type_id,
            'date_start': str(f.date_start),
            'date_end': str(f.date_end),
            'status': status
        })
    return d


###
create_form_service = Service('create form', path='forms/create', renderer='json')


@create_form_service.get(validators=(has_token, has_admin_rights))
def create_form(request):
    # we need name, form type id, date start, date end
    name = request.params['name']
    session = request.dbsession
    form_type_id = request.params['form_type_id']
    date_start = request.params['date_start']
    date_end = request.params['date_end']

    form = Form(
        name=name,
        date_start=date_start,
        date_end=date_end,
        form_type_id=form_type_id
    )
    session.add(form)

    return {'success': True}


###
delete_form_service = Service('delete form', path='forms/delete', renderer='json')


@delete_form_service.get(validators=(has_token, has_admin_rights))
def delete_form(request):
    _id = request.params['id']
    session = request.dbsession

    form = session.query(Form) \
        .filter(Form.id == _id) \
        .one()

    session.delete(form)

    return {'success': True}


###
show_form_service = Service('show form', path='forms/show', renderer='json')


@show_form_service.get(validators=(has_token, has_form_id))
def show_form(request):
    form_id = request.params.get('form_id')
    session = request.dbsession

    if form_id is None:
        return generateError('invalid form id')

    try:
        form = session.query(Form) \
            .filter(Form.id == form_id) \
            .one()
    except:
        return generateError('Invalid form id')

    d = {
        'name': form.name,
        'date_created': str(form.date_created),
        'last_modified': str(form.last_modified),
        'date_start': str(form.date_start),
        'date_end': str(form.date_end),
        'form_type_id': form.form_type_id,
        'user_type_id': form.form_type.user_type_id,
        'page_sequence': form.form_type.page_sequence
    }

    return d


###
update_form_service = Service('update form', path='forms/update', renderer='json')


@update_form_service.post()
def update_form(request):
    id = request.params['id']
    session = request.dbsession
    form = session.query(Form) \
        .filter(Form.id == id) \
        .one()

    name = request.params.get('name', None)
    if name is not None:
        form.name = name

    date_start = request.params.get('date_start', None)
    if date_start is not None:
        form.date_start = date_start

    date_end = request.params.get('date_end', None)
    if date_end is not None:
        form.date_end = date_end

    form_type_id = request.params.get('form_type_id', None)
    if form_type_id is not None:
        form.form_type_id = form_type_id

    return generateSuccess('Success')


###
get_form_types_service = Service('get form_types', path='forms/types', renderer='json')


@get_form_types_service.get()
def get_form_types(request):
    d = []
    session = request.dbsession
    for ft in session.query(FormType):
        d.append({
            'id': ft.id,
            'name': ft.name,
            'page_sequence': ft.page_sequence,
            'date_created': str(ft.date_created),
            'last_modified': str(ft.last_modified)
        })
    return d


###
print_form = Service(name='print_form', path='forms/print', description="print form")


@print_form.get()
def forms(request):
    session = request.dbsession
    _id = request.params['id']
    print _id
    ans = {}
    ####
    q_ids = session.query(Answer.element_id).filter(Answer.user_id == _id).all()
    for q_id in q_ids:
        q = session.query(Element).filter(Element.id == q_id).one()
        a = session.query(Answer).filter(Answer.element_id == q_id).filter(Answer.user_id == _id).one()
        ans[q.name] = a.text
    _u = session.query(User).filter(User.id == _id).first()
    ####
    if _u.user_type.name == 'Recommender':
        c = canvas.Canvas("form1.pdf")
        c.setLineWidth(.3)
        pdf.page(c, ans)
        c.save()
        return FileResponse('form1.pdf')
    else:
        c = canvas.Canvas("form.pdf")
        c.setLineWidth(.3)

        pdf.header(c, ans)
        pdf.ProgramOfStudy(c, ans)
        pdf.PersonalInfo(c, ans)
        pdf.EmploymentInfo(c, ans)
        pdf.AcadBg(c, ans)
        pdf.EnglishProf(c, ans)
        pdf.ProgramProf(c, ans)
        pdf.Essay(c, ans)
        pdf.References(c, ans)
        pdf.AppDec(c, ans)

        c.save()
        return FileResponse("form.pdf")
