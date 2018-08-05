from cornice import Service

from ngse.models import (
    Category,
    Form,
    form_category_association
)

get_categories_service = Service('get categories', path='forms/categories', renderer='json')


@get_categories_service.get()
def get_categories(request):
    form_id = request.params.get('form_id')
    session = request.dbsession
    form = session.query(Form) \
        .filter(Form.id == form_id) \
        .one()

    result = []

    for category in session.query(Category).join(Category.form_type, aliased=True).filter_by(id=form.form_type_id):
        result.append({
            'id': category.id,
            'name': category.name
        })

    return result


show_category_service = Service('get category', path='forms/categories/show', renderer='json')


@show_category_service.get()
def show_category(request):
    category_id = request.params.get('category_id')
    session = request.dbsession
    category = session.query(Category) \
        .filter(Category.id == category_id) \
        .one()

    d = {
        'id': category.id,
        'name': category.name,
        'date_created': str(category.date_created),
        'last_modified': str(category.last_modified),
        'form_type_ids': []
    }

    associations = session.query(form_category_association) \
        .filter(form_category_association.c.categories_id == category.id) \
        .all()

    for association in associations:
        d['form_type_ids'].append(association.form_types_id)

    return d


# @category_create.post()
# def create_category(request):
#     log.debug('{}'.format(request.params))
#     return {'hello': 'yes'}
#
#
# @category_delete.post()
# def delete_category(request):
#     log.debug('{}'.format(request.params))
#     return {'hello': 'yes'}
#
#
# @category_update.post()
# def update_category(request):
#     log.debug('{}'.format(request.params))
#     return {'hello': 'yes'}
