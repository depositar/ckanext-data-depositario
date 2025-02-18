from ckan.common import json
from ckan.lib.navl.dictization_functions import Invalid
from ckan.logic.validators import int_validator
from ckan.common import _
import re
from calendar import monthrange
from datetime import date
from datetime import datetime
from dateutil.parser import parse
from dateutil.parser import isoparse


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

    # Solr needs zero-padded month and day
    date_match = re.compile('^\d{4}(-\d{2})?(-\d{2})?$')
    date_error = _('Date format incorrect')

    if date_match.match(value):
        try:
            isoparse(value)
        except ValueError:
            errors[key] = [date_error]
    else:
        errors[key] = [date_error]

def end_time_validator(key, data, errors, context):
   """
   Raises Invalid if end time is smaller than start time.
   """

   start_time = data.get(('start_time',))
   end_time = data.get(('end_time',))

   if not start_time or not end_time:
      return

   date_validator(('start_time',), data, errors, context)
   date_validator(('end_time',), data, errors, context)

   if errors.get(('start_time',)) or errors.get(('end_time',)):
      return

   start_time_p = parse(start_time, default=datetime(1, 1, 1))
   end_time_p = parse(end_time, default=datetime(date.today().year, 12, 1))
   if len(end_time) == 7:
      # If the day of month is missing
      end_time_p = end_time_p.replace( \
            day=monthrange(end_time_p.year, end_time_p.month)[1])

   if end_time_p < start_time_p:
       raise Invalid(_('End time should be greater than \
             or equal to start time'))

def format_no_initial_period(value, context):
   """
   Raises Invalid if there is a leading period in the resource format.
   """

   if value == '':
      return value

   if value[0] == '.':
      raise Invalid(_('Format should not include the initial period. \
            Please also check other resources in this dataset.'))

   return value
