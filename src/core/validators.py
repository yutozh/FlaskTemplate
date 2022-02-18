"""
    自定义校验
"""
from collections import namedtuple
from marshmallow import ValidationError
import re


class PhoneValidator:
    message_types = namedtuple('messages', 'message')
    len_invalid = message_types('手机号长度不正确')
    regex_invalid = message_types('手机号长度不正确')

    code = 'invalid'
    phone_regex = re.compile('^1[35678]\d{9}$', re.IGNORECASE)

    def __call__(self, value):
        _m = re.match(self.phone_regex, value)
        if not bool(_m):
            raise ValidationError(self.regex_invalid.message)


phone_validator = PhoneValidator()
