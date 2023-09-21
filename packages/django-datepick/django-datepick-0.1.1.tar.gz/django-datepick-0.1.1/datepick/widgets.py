from django.forms import widgets
from django.forms.utils import to_current_timezone


class DateInput(widgets.DateInput):
    input_type = "date"


class DateTimeInput(widgets.DateTimeInput):
    input_type = "datetime-local"


class TimeInput(widgets.TimeInput):
    input_type = "time"


class SplitDateTimeWidget(widgets.MultiWidget):
    def __init__(
        self,
        attrs=None,
        date_format=None,
        time_format=None,
        date_attrs=None,
        time_attrs=None,
    ):
        widgets = (
            DateInput(
                attrs=attrs if date_attrs is None else date_attrs,
                format=date_format,
            ),
            TimeInput(
                attrs=attrs if time_attrs is None else time_attrs,
                format=time_format,
            ),
        )
        super().__init__(widgets)

    def decompress(self, value):
        if value:
            value = to_current_timezone(value)
            return [value.date(), value.time()]
        return [None, None]
