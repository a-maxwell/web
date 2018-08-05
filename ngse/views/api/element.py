from cornice import Service

from ngse.services.utils import word
from ngse.models import (
    Element
)

get_elements_service = Service('get elements', path='forms/categories/elements', renderer='json')


@get_elements_service.get()
def get_elements(request):
    category_id = request.params.get('category_id')
    result = []
    session = request.dbsession
    for element in session.query(Element).filter(Element.category_id == category_id):
        q = {
            'id': int(element.id),
            'name': element.name,
            'text': element.text,
            'klass': element.klass,
            'kind': element.kind,
            'width': word(element.width)
        }

        if (element.klass == 'question'):
            q['required'] = element.required

        if (element.choices):
            q['choices'] = element.choices

        if (element.default):
            q['default'] = element.default

        result.append(q)

    return result


# @element_create.post()
# def create_element(request):
#     log.debug('{}'.format(request.params))
#     return {'hello': 'yes'}
#
#
# @element_delete.post()
# def delete_element(request):
#     log.debug('{}'.format(request.params))
#     return {'hello': 'yes'}
#
#
# @element_show.get()
# def show_element(request):
#     log.debug('{}'.format(request.params))
#     return {'hello': 'yes'}
#
#
# @element_update.post()
# def update_element(request):
#     log.debug('{}'.format(request.params))
#     return {'hello': 'yes'}
