import logging
import jwt
import datetime
import string
import random

log = logging.getLogger(__name__)
# todo: move to settings
JWT_SECRET = "NationalGraduateSchoolOfEng'g"


def is_past(date):
    return datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S') < datetime.datetime.now()


def encode(payload):
    return jwt.encode(payload, JWT_SECRET, algorithm='HS256')


def decode(token):
    return jwt.decode(token, JWT_SECRET)


def word(n):
    if int(n) < 1:
        n = 1

    if int(n) > 16:
        n = 16

    words = [
        'zero',
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine',
        'ten',
        'eleven',
        'twelve',
        'thirteen',
        'fourteen',
        'fifteen',
        'sixteen'
    ]

    return words[n]


def password_generator(range_size=8, char_set=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(char_set) for _ in range(range_size))
