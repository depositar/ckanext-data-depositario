from ckan.common import json
from ckan.lib.navl.dictization_functions import Invalid
from ckan.logic.validators import int_validator
from ckan.common import _
import re
from datetime import datetime


def long_validator(value, context):
   """
   Raises Invalid if the given value is not a valid
   longitude coordinate.
   """
   if value is None:
      return None
   if hasattr(value, 'strip') and not value.strip():
      return None
   pattern = re.compile('^[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$')
   if re.match(pattern, value) is None:
      raise Invalid(_('Must be a valid longitude coordinate'))
   return value

def lat_validator(value, context):
   """
   Raises Invalid if the given value is not a valid
   latitude coordinate.
   """
   if value is None:
      return None
   if hasattr(value, 'strip') and not value.strip():
      return None
   pattern = re.compile('^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?)$')
   if re.match(pattern, value) is None:
      raise Invalid(_('Must be a valid latitude coordinate'))
   return value

def positive_float_validator(value, context):
   """
   Raises Invalid if the given value is not a
   positive float.
   """
   if value is None:
      return None
   if hasattr(value, 'strip') and not value.strip():
      return None

   try:
      if float(value) > 0:
         return value
   except ValueError:
      pass

   raise Invalid(_('Must be a positive float'))

def json_validator(value, context):
   """
   Raises Invalid if the given value is not a valid
   JSON string.
   """
   if value == '':
      return value
   try:
      json.loads(value)
   except ValueError:
      raise Invalid('Invalid JSON')
   return value

def date_validator(key, data, errors, context):
    """
    Raises Invalid if the given value is not
    YYYY, YYYY-MM, or YYYY-MM-DD.
    """
    value = data[key]

    is_error = [False, False, False]

    try:
        datetime.strptime(value, '%Y')
    except ValueError: is_error[0] = True
    try:
        datetime.strptime(value, '%Y-%m')
    except ValueError: is_error[1] = True
    try:
        datetime.strptime(value, '%Y-%m-%d')
    except ValueError: is_error[2] = True

    if len(set(is_error)) <= 1:
        errors[key] = [_('Date format incorrect')]
