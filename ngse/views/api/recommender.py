from cornice import Service

from ngse.services import utils
from ngse.models import (
    User
)

log = utils.log
# users/recommenders
#
# @recommender_collection.get()
# def get_recommenders(request):
#     # log.debug('{}'.format(request.params))
#     # return {'hello': 'yes'}
#     r = []
#     for user in session.query(User).filter(User.user_type_id == 4):
#         r.append({
#             'id': int(user.id),
#             'name': user.name,
#             'email': user.email,
#             'user_type': user.user_type.name,
#             'date_created': str(user.date_created),
#             'last_modified': str(user.last_modified)
#         })
#     return r
#
#
# @recommender_create.post()
# def create_recommender(request):
#     log.debug('{}'.format(request.params))
#     return {'hello': 'yes'}
#
#
# @recommender_delete.post()
# def delete_recommender(request):
#     log.debug('{}'.format(request.params))
#     return {'hello': 'yes'}
#
#
# @recommender_show.get()
# def show_recommender(request):
#     log.debug('{}'.format(request.params))
#     return {'hello': 'yes'}
#
#
# @recommender_update.post()
# def update_recommender(request):
#     log.debug('{}'.format(request.params))
#     return {'hello': 'yes'}
