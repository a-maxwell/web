import time
from .utils import encode

def generateError(message, extra_fields=None):
    d = {'success': False, 'message': message}
    if extra_fields is not None:
        d.update(extra_fields)
    return d


def generateSuccess(message, extra_fields=None):
    d = {'success': True, 'message': message}
    if extra_fields is not None:
        d.update(extra_fields)
    return d


def generateToken(user):
    current_time = int(time.time())
    expiry_time = current_time + 60 * 120

    payload = {
        'sub': user.id,
        'exp': expiry_time,
        'iat': current_time,
        'name': user.name,
        'level': user.user_type_id
    }

    token = encode(payload)

    return token
