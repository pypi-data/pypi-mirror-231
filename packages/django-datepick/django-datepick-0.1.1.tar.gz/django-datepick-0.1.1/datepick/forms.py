from django.forms import fields
from . import widgets


class DateField(fields.DateField):
    widget = widgets.DateInput


class DateTimeField(fields.DateTimeField):
    widget = widgets.DateTimeInput


class TimeField(fields.TimeField):
    widget = widgets.TimeInput
